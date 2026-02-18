# WORKFLOW KNOWLEDGE BASE FOR HEAD OF DEPARTMENT

## AGENT ROUTING PATTERNS

### Pattern 1: Statistical Comparison Requests

**Trigger Keywords:** compare, difference, between, across, groups, regions, segments, categories, test if, check if, significant

**Decision Logic:**

**Two Groups (Continuous Outcome):**
- Examples: "Compare sales between Store A and Store B", "Test if Region 1 differs from Region 2"
- Route to: Statistical_Testing_Agent → t-test (independent or paired based on context)

**Three or More Groups (Continuous Outcome):**
- Examples: "Compare sales across 5 regions", "Test if product performance differs by category"
- Route to: Statistical_Testing_Agent → One-way ANOVA

**Groups with Time Dimension:**
- Examples: "Compare monthly sales across regions", "Test if trends differ between stores"
- Route to: Ask user: "Do you want to compare overall levels (Statistical Testing) or forecast trends (Time Series)?"

**Categorical Outcome:**
- Examples: "Test if customer satisfaction rating differs by region", "Compare purchase categories across demographics"
- Route to: Statistical_Testing_Agent → Chi-square or Fisher's exact test

**Factorial/Experimental Design:**
- Examples: "Compare yield across 2 temperatures × 3 pressures"
- Keywords: factorial, design, interaction, levels, experimental
- Route to: DOE_Agent

### Pattern 2: Relationship & Modeling Requests

**Trigger Keywords:** predict, model, regression, relationship, impact, effect, influence, driver, affect, explain

**Continuous Outcome (Non-Time):**
- Examples: "Predict sales based on price and advertising", "What impacts customer satisfaction?", "Build model to explain revenue"
- Route to: Econometric_Agent

**Time-Dependent Outcome:**
- Examples: "Predict next quarter sales", "Forecast demand for next 6 months"
- Keywords: forecast, predict future, next, trend, seasonality
- Route to: TS_Agent

**Experimental Data:**
- Examples: "Model yield from factorial experiment", "Optimize process parameters"
- Keywords: experiment, optimize, factorial, DOE, response surface
- Route to: DOE_Agent

**Classification/Binary Outcome:**
- Examples: "Predict customer churn (yes/no)", "Model purchase likelihood"
- Route to: Econometric_Agent (logistic regression)

### Pattern 3: Data Quality & Exploration

**Trigger Keywords:** analyze, explore, summarize, describe, overview, quality, missing, outliers, understand data

**New Data Upload:**
- User uploads CSV file
- ALWAYS Route to: EDA_Agent (first step, mandatory)

**Data Quality Issues:**
- Examples: "Clean this data", "Handle missing values", "Remove outliers"
- EDA reports >5% missing or quality issues
- Route to: Data_processing_unit

**Exploratory Analysis:**
- Examples: "What patterns exist in this data?", "Summarize key statistics", "Understand data structure"
- Route to: EDA_Agent

### Pattern 4: Visualization Requests

**Trigger Keywords:** plot, chart, graph, visualize, heatmap, histogram, scatter, bar chart, show me

**Standalone Visualization:**
- Examples: "Create correlation heatmap", "Plot sales trend over time", "Show distribution of prices"
- No ongoing analysis context
- Route to: Visualizer_Agent

**Visualization Within Analysis:**
- Request comes during Statistical Testing/Econometric/DOE/TS analysis
- Agent creates diagnostic plots themselves
- No routing needed - current agent handles it

**Presentation Plots:**
- Examples: "Make publication-ready chart of forecast", "Create executive dashboard visualization"
- After analysis is complete
- Route to: Visualizer_Agent (optional, agent can also create)

### Pattern 5: Hypothesis Testing (Non-Comparison)

**Trigger Keywords:** test, hypothesis, check, verify, validate, normal distribution, correlation, independence, goodness of fit

**Normality Tests:**
- Examples: "Test if sales are normally distributed", "Check normality assumption"
- Context: Standalone request (not part of regression diagnostics)
- Route to: Statistical_Testing_Agent

**Correlation Tests:**
- Examples: "Test if price and sales are correlated", "Check association between variables"
- No model building requested
- Route to: Statistical_Testing_Agent

**Independence Tests:**
- Examples: "Test if gender and voting preference are independent", "Chi-square test for independence"
- Route to: Statistical_Testing_Agent

**Proportion Tests:**
- Examples: "Test if coin is fair (p=0.5)", "Compare conversion rates between campaigns"
- Route to: Statistical_Testing_Agent

### Pattern 6: Diagnostic Tests (Model-Related)

**Trigger Keywords:** heteroscedasticity, autocorrelation, multicollinearity, VIF, Durbin-Watson, Breusch-Pagan, residuals

**Regression Diagnostics:**
- Examples: "Test for heteroscedasticity in my model", "Check multicollinearity", "Verify regression assumptions"
- Context: Part of regression workflow
- Route to: Econometric_Agent (automatic in model fitting)

**Standalone Diagnostic Request:**
- Examples: "Check if residuals are autocorrelated"
- User provides residuals from external model
- Route to: Econometric_Agent (can run diagnostics on provided data)

### Pattern 7: Custom Code & Specialized Tasks

**Trigger Keywords:** run this code, execute, synthetic data, generate dummy data, custom script, merge files

**User-Provided Code:**
- User pastes Python code snippet
- "Run this exact code"
- Route to: CodeExecutor

**Synthetic Data Generation:**
- Examples: "Generate 1000 rows of fake sales data", "Create dummy dataset with trend and seasonality"
- Route to: CodeExecutor

**Specialized Libraries:**
- Tasks requiring packages not in other agents
- Web scraping, API calls
- Route to: CodeExecutor

**File Utilities:**
- Examples: "Merge these 5 CSV files", "Convert Excel to CSV"
- Route to: CodeExecutor

### Pattern 8: Market Intelligence

**Trigger Keywords:** reddit, social media, news, buzz, sentiment, trending, public opinion

**Reddit Analysis:**
- Examples: "What's trending on Reddit about electric cars?", "Sentiment analysis of recent posts on coffee brands"
- Route to: RedditNewsAgent

## MULTI-STEP WORKFLOW PATTERNS

### Workflow 1: New Data → Complete Analysis

**User Action:** Uploads CSV file

**Step-by-Step:**
1. Automatic: Route to EDA_Agent
2. EDA Output: Data structure, quality report, correlations
3. Decision Point:
   - If quality issues (>5% missing, outliers, duplicates): Route to Data_processing_unit → Return to step 1 with processed data
   - If data clean → Ask user: "What analysis would you like?"
4. User Response: Route to appropriate specialist
5. Specialist Completes → Synthesis → TERMINATE

**Example:**
User uploads "customer_churn.csv"
→ EDA: "1000 rows, 12 columns, 8% missing in 'income', outliers in 'age'"
→ DPS: Cleans data → Saves processed file
→ HOD asks: "Data is clean. What analysis?"
→ User: "Predict churn"
→ Econometric_Agent: Logistic regression
→ HOD synthesizes → TERMINATE

### Workflow 2: Statistical Testing → Visualization

**User Action:** "Compare sales across 4 regions"

**Step-by-Step:**
1. Check data availability:
   - If new data → EDA first
   - If processed data exists → Continue
2. Route to Statistical_Testing_Agent
3. Statistical_Testing runs ANOVA, returns results
4. Statistical_Testing creates diagnostic plots (Q-Q plot, residuals)
5. Decision Point: Does user want presentation plot?
   - If yes → Route to Visualizer_Agent
   - If no → Synthesis → TERMINATE

**Example:**
User: "Test if sales differ by region"
→ Statistical_Testing: One-way ANOVA, p<0.001, creates diagnostic plots
→ HOD: "Significant differences found. Need presentation plot?"
→ User: "Yes, boxplot"
→ Visualizer: Creates publication-ready boxplot
→ HOD synthesizes → TERMINATE

### Workflow 3: Regression Modeling (Full Pipeline)

**User Action:** "Model sales based on price, advertising, and seasonality"

**Step-by-Step:**
1. Check data quality → EDA/DPS if needed
2. Route to Econometric_Agent
3. Econometric Workflow:
   - Query RAG: Functional form selection
   - Load processed data
   - Curve Fitting Stage:
     - Scatter plots Y vs each X
     - Detect non-linearity
     - Test functional forms (linear, log, quadratic, cubic, exponential)
     - Compare AIC/BIC/R²
     - Show recommendation → Wait for user confirmation
   - Model Fitting:
     - Apply chosen functional form
     - Fit regression model
   - Automatic Diagnostics:
     - Heteroscedasticity test
     - Autocorrelation test
     - Multicollinearity (VIF)
     - Normality of residuals
   - If Violations: Suggest corrections (GLS, robust SE, transformations)
   - Create diagnostic plots
4. Econometric_Agent returns results
5. Optional: Visualizer for presentation plots
6. HOD synthesizes → TERMINATE

**Example:**
User: "Model revenue vs marketing spend"
→ Econometric: Curve fitting detects non-linear relationship
→ Econometric: "Data suggests log relationship. Proceed?"
→ User: "Yes"
→ Econometric: Fits log-linear model, runs diagnostics
→ Econometric: "Heteroscedasticity detected, using robust standard errors"
→ HOD synthesizes → TERMINATE

### Workflow 4: Time Series Forecasting

**User Action:** "Forecast next 6 months sales"

**Step-by-Step:**
1. Check data quality → EDA/DPS if needed
2. Route to TS_Agent
3. TS Workflow (step-by-step, NOT all at once):
   - Load data
   - Convert date column
   - Initial time series plot
   - Ask user: Aggregation level (D/W/M/Q)?
   - User responds
   - Aggregate data
   - Seasonal decomposition
   - Stationarity tests (ADF)
   - ACF/PACF plots
   - Fit ARIMA model
   - Forecast
   - Evaluate accuracy
4. TS creates all diagnostic + forecast plots
5. HOD synthesizes → TERMINATE

**Example:**
User uploads "monthly_sales.csv", asks "Forecast 6 months"
→ EDA: Time series, clean data
→ TS: Shows initial plot
→ TS: "Aggregate at Monthly level?"
→ User: "Yes"
→ TS: Decomposition shows strong seasonality
→ TS: Fits SARIMA(1,1,1)(1,1,1)[12]
→ TS: 6-month forecast with 95% CI
→ HOD synthesizes → TERMINATE

### Workflow 5: DOE Factorial Analysis

**User Action:** "Analyze 2×3 factorial experiment - Temperature and Pressure effects on Yield"

**Step-by-Step:**
1. Check if experimental data is uploaded → EDA if needed
2. Route to DOE_Agent
3. DOE Workflow:
   - Query RAG: "factorial design analysis methods"
   - Load data
   - Identify factors, levels, response
   - Calculate main effects
   - Calculate interaction effects
   - Run factorial ANOVA
   - Create plots: Main effects plot, Interaction plot, Pareto chart of effects, Normal probability plot
   - Identify optimal settings
4. DOE returns results + plots
5. HOD synthesizes → TERMINATE

**Example:**
User: "Optimize yield - 2 temps × 3 pressures"
→ DOE: Queries RAG on 2×3 factorial
→ DOE: Main effect - Temp has strongest impact
→ DOE: Interaction - Temp×Pressure significant
→ DOE: Optimal setting - Temp=200°C, Pressure=20 bar
→ HOD synthesizes → TERMINATE

### Workflow 6: Multi-Agent Collaboration

**User Action:** "Analyze sales data, test regional differences, and forecast next quarter"

**Step-by-Step:**
1. EDA_Agent → Data overview
2. Statistical_Testing_Agent → ANOVA across regions
3. TS_Agent → Quarterly forecast
4. Optional: Visualizer_Agent → Combined dashboard
5. HOD synthesizes ALL outputs → TERMINATE

**Example:**
User: "Complete analysis of regional sales"
→ EDA: 5 regions, seasonal patterns, clean data
→ Statistical_Testing: Region 1 significantly higher than others
→ TS: Overall sales forecast +8% next quarter
→ Visualizer: Dashboard with regional comparison + forecast
→ HOD: "Region 1 outperforms. Expect 8% growth. Focus expansion on underperforming regions."
→ TERMINATE

## AMBIGUITY RESOLUTION PATTERNS

### Ambiguous Request 1: "Analyze this data"

**Problem:** Too vague - what type of analysis?

**Resolution:**
HOD Response: "I can help analyze this data. What would you like to know?
1. Explore patterns and summary statistics (EDA)
2. Test hypotheses or compare groups (Statistical Testing)
3. Build predictive model (Regression/Forecasting)
4. Design or analyze experiment (DOE)
5. Create visualizations

Please specify, or describe your goal."

### Ambiguous Request 2: "Run ANOVA"

**Problem:** ANOVA context unclear - factorial experiment vs. group comparison?

**Resolution:**
Check for keywords:
- If "factorial", "design", "interaction", "levels" present → DOE_Agent
- If "compare", "groups", "regions", "categories" present → Statistical_Testing_Agent
- If unclear:
  HOD Response: "I can run ANOVA. Is this:
  1. A designed experiment with multiple factors (DOE)
  2. Comparing groups or categories (Statistical Testing)
  Please clarify the context."

### Ambiguous Request 3: "Test normality"

**Problem:** Normality of what? Data vs. residuals?

**Resolution:**
Check context:
- If regression model recently fitted → Econometric_Agent (residual normality)
- If standalone request on raw data → Statistical_Testing_Agent
- If unclear:
  HOD Response: "Test normality of:
  1. Raw data distribution (Statistical Testing)
  2. Model residuals (Econometric Diagnostics)
  Which applies to your situation?"

### Ambiguous Request 4: "Predict sales"

**Problem:** Time series forecast vs. regression model?

**Resolution:**
Check for temporal keywords:
- "next month", "future", "forecast", "upcoming" → TS_Agent
- "based on", "using", "price", "advertising" (predictors) → Econometric_Agent
- If unclear:
  HOD Response: "Predict sales based on:
  1. Historical time patterns (Time Series Forecast)
  2. Other variables like price, marketing (Regression Model)
  Which approach fits your need?"

### Ambiguous Request 5: "Create plot"

**Problem:** Diagnostic plot (agent creates) vs. presentation plot (Visualizer)?

**Resolution:**
Check context:
- If ongoing analysis (Statistical/Econometric/DOE/TS) → Current agent creates
- If standalone request with no active analysis → Visualizer_Agent
- If unclear:
  HOD Response: "Create plot for:
  1. Current analysis diagnostics (automatic)
  2. Standalone visualization request
  Assuming standalone - routing to Visualizer."

## EDGE CASES & ERROR HANDLING

### Edge Case 1: Agent Returns Error

**Scenario:** Agent fails to execute code or analysis

**HOD Response:**
1. Diagnose error type:
   - Data issue (missing columns, wrong format): Route to Data_processing_unit
   - Code/library issue: Try CodeExecutor as fallback
   - Conceptual misunderstanding: Ask user to clarify request
2. Communicate clearly:
   "The analysis encountered an issue: [error description].
   This suggests: [diagnosis]
   I recommend: [action]
   Would you like me to proceed?"

### Edge Case 2: User Dissatisfied with Output

**Scenario:** User says "This isn't what I wanted"

**HOD Response:**
"I want to get this right. Could you clarify:
1. Is the analysis approach wrong? (Need different agent/method)
2. Is the output format not helpful? (Need different visualization/summary)
3. Is something missing? (Need additional analysis)

Please describe what you expected vs. what you received."

Action: Based on response, re-route or re-query with clarification

### Edge Case 3: Insufficient Data

**Scenario:** Agent reports data too small for analysis

**Example:** 10 observations for time series forecast

**HOD Response:**
"The dataset has only [N] observations, which is insufficient for reliable [analysis type].

Recommendations:
1. Collect more data (need at least [M] observations)
2. Try simpler analysis approach
3. Use descriptive statistics instead of modeling

How would you like to proceed?"

### Edge Case 4: Assumption Violations

**Scenario:** Econometric_Agent reports violations (heteroscedasticity, autocorrelation)

**HOD Response:**
"The analysis detected [violation]. This affects [impact].

The model has applied corrections: [correction method]

Recommendations:
1. Results are now reliable with [correction applied]
2. Alternative: Try [different model approach]
3. Caution: [limitation to note]

Do you want to proceed with corrected results or try alternative?"

### Edge Case 5: Contradictory Results

**Scenario:** Multiple agents provide conflicting insights

**Example:** EDA shows no correlation, but regression finds significant effect

**HOD Response:**
"Interesting finding - we have apparent contradiction:
- [Agent 1]: [Finding 1]
- [Agent 2]: [Finding 2]

This can occur when: [explanation, e.g., confounding, non-linearity, Simpson's paradox]

Recommendation: [deeper investigation or clarification]

Would you like me to investigate further?"

## SPECIAL ROUTING SCENARIOS

### Scenario 1: User Requests Specific Agent

**User:** "Use econometric agent to analyze this"

**HOD Action:**
- Honor request UNLESS clearly wrong agent
- If clearly wrong (e.g., "use econometric for time series forecast"):
  "Econometric Agent handles regression models. For forecasting, Time Series Agent would be more appropriate.
  Would you like me to use TS_Agent instead, or do you have a specific regression approach in mind?"

### Scenario 2: Sequential Analysis Requests

**User:** First asks for EDA, then says "Now forecast this"

**HOD Action:**
- Context-aware routing
- No need to repeat EDA
- Use processed data from previous step
- Route directly to TS_Agent

### Scenario 3: Iterative Refinement

**User:** "Try different model", "Use log transformation", "Test another approach"

**HOD Action:**
- Stay with same agent
- Pass refinement instruction
- Don't re-route unless fundamentally different analysis needed

## CONFIDENCE ASSESSMENT GUIDELINES

When synthesizing outputs, assess confidence based on:

### High Confidence
- Large sample size (n>100 for regression, n>50 for time series)
- Assumptions met or violations corrected
- Model fit strong (R²>0.7 for prediction, MAPE<10% for forecast)
- Results consistent with theory/expectations
- Clean data with <5% missing

### Medium Confidence
- Moderate sample size (n=30-100)
- Minor assumption violations with corrections
- Moderate fit (R²=0.4-0.7, MAPE=10-20%)
- Some unexpected results requiring interpretation
- 5-15% missing data (handled)

### Low Confidence
- Small sample size (n<30)
- Major assumption violations uncorrected
- Poor fit (R²<0.4, MAPE>20%)
- Results contradict theory without explanation
- >15% missing or data quality issues

## HANDOFF DECISION RULES

### When to Handoff to Another Agent

**Rule 1:** Task is outside current agent's scope
Example: Statistical_Testing completes, user asks "Now forecast" → TS_Agent

**Rule 2:** Quality issues block analysis
Example: Any agent detects data issues → Data_processing_unit

**Rule 3:** Visualization needed
Example: Analysis complete, user requests "Make dashboard" → Visualizer_Agent

**Rule 4:** User explicitly requests different analysis
Example: Mid-analysis user says "Actually, let's try DOE instead"

### When NOT to Handoff

**Rule 1:** Current agent can handle refinement
Example: "Try quadratic instead of linear" → Econometric_Agent continues

**Rule 2:** Request is for clarification/explanation
Example: "What does p-value mean?" → HOD explains, no handoff

**Rule 3:** Visualization is diagnostic (part of analysis)
Example: Residual plots → Current agent creates them

## TERMINATION CONDITIONS

### Successful Termination

TERMINATE when:
1. Analysis is complete
2. Results synthesized in business terms
3. No pending user questions
4. Recommendations provided

### Premature Termination (Avoid)

Do NOT TERMINATE if:
1. Analysis encountered error (must resolve or explain)
2. User question remains unanswered
3. Ambiguity not resolved
4. Results not synthesized into actionable insights

## KEYWORDS INDEX

**EDA_Agent:**
analyze, explore, summarize, describe, statistics, overview, quality, structure, understand data

**Data_processing_unit:**
clean, process, transform, missing values, outliers, duplicates, normalize, standardize, impute

**Statistical_Testing_Agent:**
t-test, ANOVA, chi-square, test, compare groups, difference, hypothesis, normality, correlation, independence, proportion, Fisher, Mann-Whitney, Kruskal-Wallis

**Econometric_Agent:**
regression, OLS, GLS, model, predict (non-time), relationship, impact, effect, driver, logistic, heteroscedasticity, multicollinearity, autocorrelation, diagnostics

**DOE_Agent:**
factorial, design of experiments, DOE, optimize, response surface, Taguchi, main effects, interaction, experimental design, screening, levels, factors

**TS_Agent:**
forecast, time series, ARIMA, predict future, trend, seasonality, next month/quarter/year, decomposition, stationarity

**Visualizer_Agent:**
plot, chart, graph, visualize, heatmap, histogram, scatter, bar chart, dashboard (standalone requests)

**CodeExecutor:**
run code, execute, synthetic data, generate dummy, custom script, merge files, special libraries

**RedditNewsAgent:**
reddit, social media, news, buzz, sentiment, trending, public opinion