# debug_graphrag.py
"""Debug script to see what subprocess captures"""

import subprocess
import os
from datetime import datetime

def debug_graphrag_global():
    print("Running GraphRAG Global with debug output...")
    print("=" * 60)
    
    cmd = [
        "graphrag",
        "query",
        "--root", r"F:\Project work\Cafe Restaurant Analysis\Agents\DOE Brain\Grag",
        "--method", "global",
        "--query", "What is a factorial design?"
    ]
    
    print("Executing command...")
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=600,
        encoding='utf-8',
        errors='replace'
    )
    
    # Save raw outputs
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    stdout_file = f"debug_stdout_{timestamp}.txt"
    stderr_file = f"debug_stderr_{timestamp}.txt"
    
    with open(stdout_file, 'w', encoding='utf-8') as f:
        f.write(result.stdout)
    
    with open(stderr_file, 'w', encoding='utf-8') as f:
        f.write(result.stderr)
    
    print(f"\n✅ Saved raw outputs:")
    print(f"   stdout: {stdout_file} ({len(result.stdout)} chars)")
    print(f"   stderr: {stderr_file} ({len(result.stderr)} chars)")
    print(f"   returncode: {result.returncode}")
    
    print("\n" + "=" * 60)
    print("STDOUT Preview (first 500 chars):")
    print("=" * 60)
    print(result.stdout[:500])
    
    print("\n" + "=" * 60)
    print("STDERR Preview (first 500 chars):")
    print("=" * 60)
    print(result.stderr[:500])
    
    print("\n" + "=" * 60)
    
    if len(result.stdout) < 100:
        print("⚠️  WARNING: stdout is very short or empty!")
        print("   The content might be in stderr instead.")
    else:
        print("✅ stdout has content")
    
    if "## Understanding" in result.stdout or "# Understanding" in result.stdout:
        print("✅ Found content marker in stdout!")
    elif "## Understanding" in result.stderr or "# Understanding" in result.stderr:
        print("⚠️  Content is in stderr, not stdout!")
        print("   This is the problem - need to check stderr for content too!")
    else:
        print("❌ Content marker not found in either stdout or stderr")
        print("   Check the saved files manually")

if __name__ == "__main__":
    debug_graphrag_global()