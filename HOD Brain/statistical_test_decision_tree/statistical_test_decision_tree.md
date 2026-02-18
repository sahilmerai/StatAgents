# STATISTICAL TEST SELECTION GUIDE

## DECISION TREE FOR CHOOSING THE RIGHT TEST

### START: What is your research question?

**Branch 1: Comparing Means/Medians**
→ Go to Section A: Comparison Tests

**Branch 2: Testing Relationships/Associations**
→ Go to Section B: Relationship Tests

**Branch 3: Testing Distributions**
→ Go to Section C: Distribution Tests

**Branch 4: Testing Proportions**
→ Go to Section D: Proportion Tests

---

## SECTION A: COMPARISON TESTS

### Question: How many groups are you comparing?

#### A1: Two Groups (Continuous Outcome)

**Decision Point: Are samples independent or paired?**

**Independent Samples (different subjects in each group):**
- Example: Compare sales between Store A and Store B
- Example: Test if Drug A produces different blood pressure than Drug B

**Check normality first:**
- Both groups normally distributed → **Independent Samples t-test**
- Either group non-normal → **Mann-Whitney U test** (non-parametric alternative)

**Independent Samples t-test:**
```
Assumptions:
- Independent observations
- Continuous outcome variable
- Approximately normal distribution in each group
- Homogeneity of variance (Levene's test)

Python code:
from scipy.stats import ttest_ind, levene
# Check equal variances
stat, p_var = levene(group1, group2)
# Run t-test
if p_var > 0.05:
    stat, p = ttest_ind(group1, group2)  # Equal variances
else:
    stat, p = ttest_ind(group1, group2, equal_var=False)  # Welch's t-test

Interpretation:
- p < 0.05: Groups differ significantly
- t-statistic: Magnitude of difference (larger = stronger)
- Report: t(df) = value, p = value, mean difference with 95% CI
```

**Mann-Whitney U test:**
```
Use when:
- Non-normal distributions
- Ordinal data
- Outliers present
- Small sample sizes (n<30 per group)

Python code:
from scipy.stats import mannwhitneyu
stat, p = mannwhitneyu(group1, group2, alternative='two-sided')

Interpretation:
- p < 0.05: Groups have different distributions
- Reports median difference, not mean
- More robust to outliers than t-test
```

**Paired Samples (same subjects measured twice):**
- Example: Before/after treatment comparison
- Example: Test scores at start vs. end of semester

**Check normality of differences:**
- Differences normally distributed → **Paired Samples t-test**
- Differences non-normal → **Wilcoxon Signed-Rank test**

**Paired Samples t-test:**
```
Assumptions:
- Paired observations (same subject, two measurements)
- Continuous outcome
- Differences approximately normally distributed

Python code:
from scipy.stats import ttest_rel
stat, p = ttest_rel(before, after)

Interpretation:
- p < 0.05: Significant change from before to after
- Mean difference indicates direction and magnitude
- Report: t(df) = value, p = value, mean difference
```

**Wilcoxon Signed-Rank test:**
```
Use when:
- Paired data with non-normal differences
- Ordinal paired data
- Small samples

Python code:
from scipy.stats import wilcoxon
stat, p = wilcoxon(before, after)

Interpretation:
- p < 0.05: Significant change in median values
- Non-parametric alternative to paired t-test
```

#### A2: Three or More Groups (Continuous Outcome)

**One Factor (Independent Groups):**
- Example: Compare sales across 5 regions
- Example: Test if satisfaction differs by age group (young/middle/old)

**Check assumptions:**
- Normal distributions + equal variances → **One-Way ANOVA**
- Violated assumptions → **Kruskal-Wallis test**

**One-Way ANOVA:**
```
Assumptions:
- Independent groups
- Continuous outcome
- Normal distribution within each group
- Homogeneity of variance (Levene's test)

Python code:
from scipy.stats import f_oneway, levene
# Check equal variances
stat_var, p_var = levene(group1, group2, group3)
# Run ANOVA
stat, p = f_oneway(group1, group2, group3)

# Post-hoc tests (if ANOVA significant)
from statsmodels.stats.multicomp import pairwise_tukeyhsd
posthoc = pairwise_tukeyhsd(data['outcome'], data['group'])
print(posthoc)

Interpretation:
- p < 0.05: At least one group differs from others
- F-statistic: Ratio of between-group to within-group variance
- Post-hoc tests identify which specific groups differ
- Report: F(df_between, df_within) = value, p = value
```

**Kruskal-Wallis test:**
```
Use when:
- Three or more independent groups
- Non-normal distributions
- Ordinal outcome variable
- Unequal variances

Python code:
from scipy.stats import kruskal
stat, p = kruskal(group1, group2, group3)

# Post-hoc (Dunn's test)
from scikit_posthocs import posthoc_dunn
posthoc = posthoc_dunn([group1, group2, group3])

Interpretation:
- p < 0.05: At least one group has different median
- Non-parametric alternative to ANOVA
- Post-hoc tests needed to identify which groups differ
```

**Two Factors (Factorial Design):**
- Example: Test effect of Temperature (2 levels) AND Pressure (3 levels) on Yield
- Example: Sales by Region (5) × Season (4)

**This is DOE territory → Route to DOE_Agent**

**Two-Way ANOVA:**
```
Use for:
- Two categorical independent variables (factors)
- Testing main effects and interactions
- Balanced or unbalanced designs

Python code:
import statsmodels.api as sm
from statsmodels.formula.api import ols

model = ols('outcome ~ C(factor1) + C(factor2) + C(factor1):C(factor2)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

Interpretation:
- Main effect Factor1: Does Factor1 affect outcome (averaging across Factor2)?
- Main effect Factor2: Does Factor2 affect outcome (averaging across Factor1)?
- Interaction: Do effects of Factor1 depend on levels of Factor2?
- p < 0.05 for each effect indicates significance
```

**Repeated Measures (Same Subjects, Multiple Times):**
- Example: Test scores measured at 4 time points (Week 1, 2, 3, 4)
- Example: Blood pressure measured under 3 different drug conditions

**Repeated Measures ANOVA:**
```
Use when:
- Same subjects measured multiple times
- More than 2 time points or conditions
- Continuous outcome

Python code:
from statsmodels.stats.anova import AnovaRM
model = AnovaRM(df, depvar='outcome', subject='subject_id', within=['time'])
results = model.fit()
print(results)

Interpretation:
- Tests if outcome changes across time/conditions
- Accounts for correlation within subjects
- p < 0.05: Significant change across time points
```

---

## SECTION B: RELATIONSHIP TESTS

### Question: What types of variables are you testing?

#### B1: Two Continuous Variables

**Testing correlation (strength and direction of linear relationship):**

**Check distribution:**
- Both normally distributed → **Pearson correlation**
- Either non-normal OR ordinal → **Spearman correlation**
- Monotonic but non-linear → **Spearman correlation**

**Pearson Correlation:**
```
Assumptions:
- Both variables continuous
- Linear relationship
- Bivariate normal distribution
- No extreme outliers

Python code:
from scipy.stats import pearsonr
r, p = pearsonr(variable1, variable2)

Interpretation:
- r ranges from -1 to +1
- r > 0: Positive relationship (both increase together)
- r < 0: Negative relationship (one increases, other decreases)
- |r| > 0.7: Strong correlation
- |r| 0.4-0.7: Moderate correlation
- |r| < 0.4: Weak correlation
- p < 0.05: Correlation is statistically significant
- R² = r²: Proportion of shared variance

Report: r = value, p = value, R² = value
```

**Spearman Correlation:**
```
Use when:
- Ordinal variables
- Non-linear but monotonic relationships
- Non-normal distributions
- Presence of outliers

Python code:
from scipy.stats import spearmanr
rho, p = spearmanr(variable1, variable2)

Interpretation:
- rho (ρ) ranges from -1 to +1 (same as Pearson r)
- Tests monotonic relationship (not just linear)
- More robust to outliers
- Report: ρ = value, p = value
```

**Kendall's Tau:**
```
Use when:
- Small sample size
- Many tied ranks
- Ordinal data with ties

Python code:
from scipy.stats import kendalltau
tau, p = kendalltau(variable1, variable2)

Interpretation:
- tau (τ) ranges from -1 to +1
- More conservative than Spearman
- Better for small samples
```

#### B2: Two Categorical Variables

**Testing association/independence:**

**Chi-Square Test of Independence:**
```
Use when:
- Both variables categorical
- Testing if variables are independent
- Expected frequencies ≥ 5 in each cell

Python code:
from scipy.stats import chi2_contingency
# Create contingency table
contingency_table = pd.crosstab(df['var1'], df['var2'])
chi2, p, dof, expected = chi2_contingency(contingency_table)

Interpretation:
- p < 0.05: Variables are associated (not independent)
- Chi-square value: Magnitude of departure from independence
- Check expected frequencies: all should be ≥ 5
- If violated, use Fisher's Exact Test
- Report: χ²(df) = value, p = value

Effect size (Cramér's V):
n = contingency_table.sum().sum()
cramers_v = np.sqrt(chi2 / (n * (min(contingency_table.shape) - 1)))
```

**Fisher's Exact Test:**
```
Use when:
- 2×2 contingency table
- Small sample sizes
- Expected frequencies < 5

Python code:
from scipy.stats import fisher_exact
# For 2x2 table only
oddsratio, p = fisher_exact([[a, b], [c, d]])

Interpretation:
- p < 0.05: Significant association
- Odds ratio: Strength of association
- Exact test (no large-sample approximation needed)
- Report: Odds Ratio = value, p = value (Fisher's exact)
```

#### B3: One Continuous, One Categorical Variable

**This is typically handled by:**
- **Comparison tests (t-test, ANOVA)** if goal is group comparison
- **Regression** if goal is prediction (Route to Econometric_Agent)

**Point-Biserial Correlation:**
```
Use when:
- One continuous variable
- One dichotomous (binary) categorical variable
- Checking correlation between continuous and binary

Python code:
from scipy.stats import pointbiserialr
# Binary variable must be coded 0/1
r, p = pointbiserialr(df['binary'], df['continuous'])

Interpretation:
- r ranges from -1 to +1
- Equivalent to Pearson r with binary variable
- p < 0.05: Significant correlation
```

---

## SECTION C: DISTRIBUTION TESTS

### Question: What property of the distribution are you testing?

#### C1: Testing Normality

**For sample sizes n < 50:**

**Shapiro-Wilk Test:**
```
Best for:
- Small to moderate samples (n < 50)
- Most powerful normality test
- Testing if data comes from normal distribution

Python code:
from scipy.stats import shapiro
stat, p = shapiro(data)

Interpretation:
- H0: Data is normally distributed
- p > 0.05: Fail to reject H0 (data appears normal)
- p < 0.05: Reject H0 (data not normal)
- Note: Very sensitive to small deviations in large samples
- Always pair with visual inspection (Q-Q plot, histogram)
- Report: W = value, p = value
```

**For sample sizes n ≥ 50:**

**Anderson-Darling Test:**
```
Best for:
- Moderate to large samples
- More weight on tail regions
- Detects departures in tails

Python code:
from scipy.stats import anderson
result = anderson(data, dist='norm')

Interpretation:
- Compare statistic to critical values at different significance levels
- If statistic > critical value: Reject normality
- More sensitive to tails than Shapiro-Wilk
```

**Kolmogorov-Smirnov Test:**
```
Use for:
- Large samples (n > 50)
- Testing fit to any distribution (not just normal)
- Less powerful than Shapiro-Wilk for normality

Python code:
from scipy.stats import kstest
stat, p = kstest(data, 'norm')

Interpretation:
- p > 0.05: Data consistent with specified distribution
- p < 0.05: Data does not fit distribution
- Can test against distributions other than normal
```

**Visual Assessment (Always Recommended):**
```python
import matplotlib.pyplot as plt
from scipy import stats

# Q-Q plot
stats.probplot(data, dist="norm", plot=plt)
plt.title('Q-Q Plot')
plt.show()

# Histogram with normal curve overlay
plt.hist(data, bins=30, density=True, alpha=0.7)
mu, sigma = data.mean(), data.std()
x = np.linspace(data.min(), data.max(), 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2)
plt.title('Histogram vs. Normal Distribution')
plt.show()
```

#### C2: Testing Equality of Variances

**Levene's Test:**
```
Use when:
- Testing if two or more groups have equal variances
- Before ANOVA or t-test (assumption check)
- Robust to non-normality

Python code:
from scipy.stats import levene
stat, p = levene(group1, group2, group3)

Interpretation:
- H0: All groups have equal variance
- p > 0.05: Equal variances (homoscedasticity)
- p < 0.05: Unequal variances (heteroscedasticity)
- If p < 0.05: Use Welch's test instead of standard ANOVA/t-test
```

**Bartlett's Test:**
```
Use when:
- Testing equal variances
- Data is normally distributed
- More powerful than Levene if normality holds
- Very sensitive to non-normality

Python code:
from scipy.stats import bartlett
stat, p = bartlett(group1, group2, group3)

Interpretation:
- Same as Levene, but assumes normality
- Don't use if normality violated
```

#### C3: Goodness of Fit Tests

**Chi-Square Goodness of Fit:**
```
Use when:
- Testing if observed frequencies match expected frequencies
- Categorical outcome
- Expected frequencies ≥ 5

Example: Test if dice is fair (equal probability for all 6 outcomes)

Python code:
from scipy.stats import chisquare
# observed = actual counts
# expected = expected counts under null hypothesis
chi2, p = chisquare(f_obs=observed, f_exp=expected)

Interpretation:
- p > 0.05: Data fits expected distribution
- p < 0.05: Data does not fit expected distribution
- Report: χ²(df) = value, p = value
```

---

## SECTION D: PROPORTION TESTS

### Question: How many proportions/groups?

#### D1: Single Proportion

**Binomial Test:**
```
Use when:
- Testing if observed proportion differs from expected
- Binary outcome (success/failure)
- Example: Is coin fair? (test if p = 0.5)

Python code:
from scipy.stats import binom_test
# Alternative in newer versions:
from scipy.stats import binomtest
p_value = binomtest(k=successes, n=trials, p=expected_proportion, alternative='two-sided').pvalue

Interpretation:
- H0: True proportion = expected proportion
- p < 0.05: Observed proportion significantly different from expected
- Example: 60 heads in 100 flips, test if p=0.5
  binomtest(60, 100, 0.5) → p = 0.057 (not significant)
```

#### D2: Two Proportions

**Two-Proportion Z-Test:**
```
Use when:
- Comparing proportions between two independent groups
- Example: Compare conversion rates between two campaigns
- Large samples (np ≥ 5, n(1-p) ≥ 5 for both groups)

Python code:
from statsmodels.stats.proportion import proportions_ztest
count = np.array([successes_group1, successes_group2])
nobs = np.array([n_group1, n_group2])
stat, p = proportions_ztest(count, nobs)

Interpretation:
- p < 0.05: Proportions differ significantly
- z-statistic: Standardized difference
- Report: z = value, p = value, proportion difference with CI
```

**Fisher's Exact Test (for small samples):**
```
See Section B2 for details
Use when sample sizes small or expected frequencies < 5
```

#### D3: Multiple Proportions

**Chi-Square Test:**
```
Use when:
- Comparing proportions across 3+ groups
- Example: Test if satisfaction (yes/no) differs across 4 regions
- See Section B2 for Chi-Square details
```

---

## SECTION E: SPECIAL CASES

### E1: Multiple Comparisons Problem

**When testing multiple hypotheses simultaneously:**

**Problem:**
- Testing 20 comparisons at α=0.05 → expect 1 false positive by chance
- False discovery rate increases with number of tests

**Solutions:**

**Bonferroni Correction:**
```
Adjusted α = original α / number of comparisons

Example:
- 10 pairwise comparisons, α = 0.05
- Bonferroni α = 0.05 / 10 = 0.005
- Only reject H0 if p < 0.005

Python code:
from statsmodels.stats.multitest import multipletests
# p_values = list of p-values from multiple tests
reject, p_adjusted, _, _ = multipletests(p_values, method='bonferroni')

Pros: Simple, controls family-wise error rate
Cons: Very conservative (reduces power)
```

**Holm-Bonferroni (less conservative):**
```python
reject, p_adjusted, _, _ = multipletests(p_values, method='holm')
```

**False Discovery Rate (FDR) - Benjamini-Hochberg:**
```python
reject, p_adjusted, _, _ = multipletests(p_values, method='fdr_bh')

# More appropriate when:
# - Many tests conducted
# - Willing to accept some false positives
# - Exploratory research
```

### E2: Power Analysis

**Determining required sample size:**

**For t-test:**
```python
from statsmodels.stats.power import ttest_power, tt_solve_power

# Calculate required sample size
n = tt_solve_power(effect_size=0.5, alpha=0.05, power=0.8, alternative='two-sided')

# Calculate power given sample size
power = ttest_power(effect_size=0.5, nobs=50, alpha=0.05, alternative='two-sided')

Interpretation:
- effect_size: Cohen's d (0.2=small, 0.5=medium, 0.8=large)
- alpha: Significance level (usually 0.05)
- power: Probability of detecting effect if it exists (usually 0.8)
- nobs: Sample size per group
```

**For ANOVA:**
```python
from statsmodels.stats.power import ftest_power, ftest_anova_power

# Calculate power
power = ftest_anova_power(effect_size=0.25, nobs=30, alpha=0.05, k_groups=3)
```

### E3: Effect Size Measures

**Always report effect sizes alongside p-values:**

**Cohen's d (for t-tests):**
```python
def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std

# Interpretation:
# d = 0.2: Small effect
# d = 0.5: Medium effect
# d = 0.8: Large effect
```

**Eta-squared (for ANOVA):**
```python
# η² = SS_between / SS_total
# Proportion of variance explained by group membership

# Interpretation:
# η² = 0.01: Small effect
# η² = 0.06: Medium effect
# η² = 0.14: Large effect
```

**Cramér's V (for Chi-square):**
```python
def cramers_v(chi2, n, k):
    """
    chi2: Chi-square statistic
    n: Total sample size
    k: Minimum of (rows-1, columns-1)
    """
    return np.sqrt(chi2 / (n * k))

# Interpretation (for 2x2 table):
# V = 0.1: Small effect
# V = 0.3: Medium effect
# V = 0.5: Large effect
```

---

## DECISION FLOWCHART SUMMARY
```
START: What is your goal?

├─ Compare groups/conditions
│  ├─ 2 groups
│  │  ├─ Independent → t-test (normal) or Mann-Whitney (non-normal)
│  │  └─ Paired → Paired t-test (normal) or Wilcoxon (non-normal)
│  │
│  └─ 3+ groups
│     ├─ One factor → ANOVA (normal) or Kruskal-Wallis (non-normal)
│     └─ Two+ factors → Two-way ANOVA or DOE_Agent
│
├─ Test relationships
│  ├─ Both continuous → Pearson (normal) or Spearman (non-normal)
│  ├─ Both categorical → Chi-square or Fisher's exact
│  └─ Mixed → Point-biserial or t-test/ANOVA
│
├─ Test distributions
│  ├─ Normality → Shapiro-Wilk (n<50) or Anderson-Darling (n≥50)
│  ├─ Equal variances → Levene or Bartlett
│  └─ Goodness of fit → Chi-square GOF
│
└─ Test proportions
   ├─ Single proportion → Binomial test
   ├─ Two proportions → Two-proportion z-test or Fisher's exact
   └─ Multiple proportions → Chi-square test
```

---

## COMMON PITFALLS & REMINDERS

### Pitfall 1: Confusing Correlation with Causation
- Correlation only shows association, not causation
- Always consider confounding variables
- Use language: "associated with", "related to", not "causes"

### Pitfall 2: Ignoring Assumptions
- Every test has assumptions - check them!
- Violated assumptions → invalid conclusions
- Use non-parametric alternatives when needed

### Pitfall 3: Over-relying on p-values
- p-value measures statistical significance, not practical importance
- Always report effect sizes
- Consider confidence intervals

### Pitfall 4: Multiple Testing Without Correction
- Testing many hypotheses inflates Type I error rate
- Use Bonferroni, FDR, or other corrections
- Report both raw and adjusted p-values

### Pitfall 5: Small Sample Sizes
- Underpowered studies fail to detect real effects
- Conduct power analysis before collecting data
- Be cautious interpreting non-significant results with small n

### Pitfall 6: Cherry-Picking Results
- Don't test multiple outcomes and report only significant ones
- Pre-register hypotheses when possible
- Report all tests conducted

### Pitfall 7: Misinterpreting Non-Significance
- p > 0.05 ≠ "no effect"
- Could be: true null, insufficient power, high variance
- Report: "no evidence of effect" not "no effect exists"

---

## QUICK REFERENCE TABLE

| Research Question | Data Type | Test | Python Function |
|------------------|-----------|------|----------------|
| Compare 2 groups (independent) | Continuous, normal | Independent t-test | `scipy.stats.ttest_ind` |
| Compare 2 groups (independent) | Continuous, non-normal | Mann-Whitney U | `scipy.stats.mannwhitneyu` |
| Compare 2 groups (paired) | Continuous, normal | Paired t-test | `scipy.stats.ttest_rel` |
| Compare 2 groups (paired) | Continuous, non-normal | Wilcoxon signed-rank | `scipy.stats.wilcoxon` |
| Compare 3+ groups | Continuous, normal | One-way ANOVA | `scipy.stats.f_oneway` |
| Compare 3+ groups | Continuous, non-normal | Kruskal-Wallis | `scipy.stats.kruskal` |
| Association (2 continuous) | Continuous, normal | Pearson correlation | `scipy.stats.pearsonr` |
| Association (2 continuous) | Continuous, non-normal | Spearman correlation | `scipy.stats.spearmanr` |
| Association (2 categorical) | Categorical | Chi-square | `scipy.stats.chi2_contingency` |
| Association (2 categorical, small n) | Categorical, 2×2 | Fisher's exact | `scipy.stats.fisher_exact` |
| Test normality (n<50) | Continuous | Shapiro-Wilk | `scipy.stats.shapiro` |
| Test normality (n≥50) | Continuous | Anderson-Darling | `scipy.stats.anderson` |
| Test equal variances | Continuous | Levene | `scipy.stats.levene` |
| Test single proportion | Binary | Binomial test | `scipy.stats.binomtest` |
| Test 2 proportions | Binary | Two-proportion z-test | `statsmodels.stats.proportion.proportions_ztest` |
| Goodness of fit | Categorical | Chi-square GOF | `scipy.stats.chisquare` |