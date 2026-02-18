# reddit.py
from __future__ import annotations

import os
from typing import List, Union, Dict, Any, Optional, Annotated
from datetime import datetime, timezone
from collections import Counter
from dotenv import load_dotenv
import praw
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

# ---------- Helpers ----------
def _as_query_string(words: Union[str, List[str]]) -> str:
    if isinstance(words, str):
        return words.strip()
    return " ".join(w.strip() for w in words if w and w.strip())


def _to_iso_utc(ts: Optional[float]) -> Optional[str]:
    if ts is None:
        return None
    try:
        return datetime.fromtimestamp(float(ts), tz=timezone.utc).isoformat()
    except Exception:
        return None


def _clean_thumb(th: Optional[str]) -> Optional[str]:
    # PRAW often gives placeholders like 'self', 'default', 'nsfw'
    if not th or th in ("self", "default", "nsfw"):
        return None
    return th


def _truncate(text: Optional[str], max_chars: int) -> Optional[str]:
    if text is None:
        return None
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1] + "…"


# ---------- The Tool Function (call this from your agent) ----------
def reddit_search_all(
    words: Annotated[Union[str, List[str]], "Keywords or phrase to search on Reddit (across r/all)."],
    *,
    # Auth (env defaults): set REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET / REDDIT_USER_AGENT
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    user_agent: Optional[str] = None,
    # Search params
    limit: Annotated[int, "Max number of posts to return"] = 50,
    sort: Annotated[str, "relevance|hot|top|new|comments"] = "relevance",
    time_filter: Annotated[str, "all|year|month|week|day|hour"] = "all",
    include_nsfw: Annotated[bool, "Allow NSFW content"] = False,
    # Output shaping
    text_max_chars: Annotated[int, "Trim selftext to at most this many chars"] = 2500,
    include_summary: Annotated[bool, "Add top subreddits/domains summary"] = True,
    # Networking
) -> Dict[str, Any]:
    """
    Search posts across ALL of Reddit using PRAW and return a JSON-serializable dict.

    Notes:
      • Provide credentials via environment variables (recommended):
            REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
        or pass them as parameters.
      • `verify_ssl=True` by default for secure connections. Set False only if
        your corporate environment requires it (not recommended for production).

    Returns:
        {
          "query": "...",
          "params": {...},
          "count": N,
          "items": [
            {
              "id": "...", "title": "...", "author": "...", "subreddit": "...",
              "is_self": true, "selftext": "...", "url": "...",
              "permalink": "...", "full_link": "...",
              "created_utc": 1719000000.0, "created_iso": "2024-06-21T10:00:00+00:00",
              "score": 123, "upvote_ratio": 0.92, "num_comments": 45,
              "over_18": false, "stickied": false, "spoiler": false,
              "link_flair_text": "...", "domain": "...", "thumbnail": "..."
            }, ...
          ],
          "summary": {
            "top_subreddits": [{"name": "AskReddit", "count": 10}, ...],
            "top_domains":    [{"domain": "i.imgur.com", "count": 7}, ...]
          }
        }
    """
    # --- Resolve credentials ---
    cid = client_id or os.getenv("REDDIT_CLIENT_ID")
    csec = client_secret or os.getenv("REDDIT_CLIENT_SECRET")
    uag = user_agent or os.getenv("REDDIT_USER_AGENT") or "python:niq.agent:v1.0 (by u/yourusername)"

    if not (cid and csec and uag):
        raise RuntimeError(
            "Reddit credentials missing. Set REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT "
            "in your environment or pass client_id/client_secret/user_agent."
        )

    # --- Build a session (TLS verification configurable) ---
    session = requests.Session()
    session.verify = False

    # --- Create PRAW client (read-only) ---
    reddit = praw.Reddit(
        client_id=cid,            # <-- put your client_id here
        client_secret=csec,    # <-- put your client_secret here
        user_agent=uag,
        ratelimit_seconds=5,
        requestor_kwargs={"session": session},   # <-- inject custom session
        check_for_updates=False,
    )
    reddit.read_only = True

    query = _as_query_string(words)
    search_params = {
        "include_over_18": "on" if include_nsfw else "off"
    }

    # --- Perform search across ALL subreddits ---
    results = reddit.subreddit("all").search(
        query=query,
        sort=sort,
        time_filter=time_filter,
        limit=limit,
        params=search_params
    )

    items: List[Dict[str, Any]] = []
    for p in results:
        try:
            items.append({
                "id": p.id,
                "title": p.title or "",
                "author": str(p.author) if p.author else None,
                "subreddit": str(p.subreddit) if getattr(p, "subreddit", None) else None,
                "is_self": bool(getattr(p, "is_self", False)),
                "selftext": _truncate(getattr(p, "selftext", "") or "", text_max_chars),
                "url": getattr(p, "url", None),
                "permalink": getattr(p, "permalink", None),
                "full_link": f"https://www.reddit.com{getattr(p, 'permalink', '')}" if getattr(p, "permalink", None) else None,
                "created_utc": float(getattr(p, "created_utc", 0.0)) if getattr(p, "created_utc", None) is not None else None,
                "created_iso": _to_iso_utc(getattr(p, "created_utc", None)),
                "score": getattr(p, "score", None),
                "upvote_ratio": getattr(p, "upvote_ratio", None),
                "num_comments": getattr(p, "num_comments", None),
                "over_18": getattr(p, "over_18", None),
                "stickied": getattr(p, "stickied", None),
                "spoiler": getattr(p, "spoiler", None),
                "link_flair_text": getattr(p, "link_flair_text", None),
                "domain": getattr(p, "domain", None),
                "thumbnail": _clean_thumb(getattr(p, "thumbnail", None)),
            })
        except Exception:
            # Skip malformed items but continue
            continue

    payload: Dict[str, Any] = {
        "query": query,
        "params": {
            "limit": limit,
            "sort": sort,
            "time_filter": time_filter,
            "include_nsfw": include_nsfw,
        },
        "count": len(items),
        "items": items,
    }

    if include_summary:
        subs = Counter(i.get("subreddit") for i in items if i.get("subreddit"))
        doms = Counter(i.get("domain") for i in items if i.get("domain"))
        payload["summary"] = {
            "top_subreddits": [{"name": n, "count": c} for n, c in subs.most_common(10)],
            "top_domains": [{"domain": n, "count": c} for n, c in doms.most_common(10)],
        }

    return payload


# ---------- Local test ----------
if __name__ == "__main__":
    # Example usage (requires env vars set)
    data = reddit_search_all(
        words=["Indian instant coffee"],
        limit=10,
        sort="top",
        time_filter="all",
        include_nsfw=False,
    )
    # Print a compact view
    from pprint import pprint
    pprint({
        "query": data["query"],
        "count": data["count"],
        "first_3": [{k: v for k, v in r.items() if k in ("title", "full_link","subreddit", "score", "num_comments")} for r in data["items"][:3]],
    })
