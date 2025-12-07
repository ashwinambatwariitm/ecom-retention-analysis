# E-commerce Customer Retention — 2024 Quarterly Analysis

**Author / Verification:** 24f2009283@ds.study.iitm.ac.in

## Summary (TL;DR)
We analyzed the company's quarterly customer retention rates for 2024:

- Q1: 71.14  
- Q2: 69.47  
- Q3: 71.89  
- Q4: 75.91  

**Reported average (2024): 72.1**

The industry benchmark target is **85**. The company is currently **~12.9 percentage points** below the benchmark (85 − 72.1 ≈ 12.9 pp). This is a material gap that requires a focused retention strategy combining short-term reactivation and mid-term structural improvements.

---

## What we did
1. Calculated summary statistics (average displayed as **72.1**).  
2. Plotted the quarterly trend with an industry benchmark line.  
3. Produced simple projections illustrating how many quarters are required to close the gap under different per-quarter improvement scenarios.  
4. Built a set of actionable recommendations to reach the industry target.

You can reproduce the analysis:
```bash
python3 analysis/analysis.py
# this will save visuals/retention_trend.png and analysis/analysis_summary.txt

Key findings

Recent improvement in Q4: Q4 shows the highest quarterly rate at 75.91 — a positive sign, likely driven by seasonality or recent campaigns.

Mid-year dip: Q2 is the lowest (69.47). Understanding what changed in Q2 (product mix, pricing, UX, fulfillment, campaigns) is important.

Average vs. target: The 2024 average retention is 72.1, while the industry target is 85 — a 12.9 pp gap that is non-trivial and would materially affect LTV and CAC payback.

Business implications

Revenue & LTV: Lower retention compresses customer lifetime value (LTV), meaning acquisition costs need to stay lower or ROI will decline.

Growth efficiency: To grow sustainably, the company must reduce churn and increase retention — otherwise marketing spend will scale poorly.

Operational focus: The Q2 dip suggests there may be operational or product frictions that cause cohort-specific churn.

Actionable recommendations (prioritized)
A. Immediate (0–3 months) — "Rescue & Reactivate"

Win-back campaign for lapsed customers

Segments: last purchase 3–12 months, high-value LTV cohorts prioritized.

Channels: email + push + targeted paid social.

Offer: time-limited discount or free shipping, with personalized product recommendations.

Measure: Lift in 30- and 90-day reactivation rates and cost per reactivated customer.

Customer feedback loop

Send a short survey (NPS + 1 open question) to customers who churned in Q2–Q3.

Prioritize categorization of reasons (price, product quality, delivery, UX).

Onboarding & first 30 days improvements

Ensure onboarding flows highlight value (welcome series, how-to guides).

A quick A/B test: optimized onboarding sequence vs current.

B. Medium term (3–9 months) — "Strengthen Product/Experience"

Cohort analysis & root-cause diagnosis

Perform cohort retention by acquisition channel, product category, and geography.

Identify cohorts with the steepest drop-off and prioritize remediation.

Personalization & recommendation engine

Improve product recommendations (cross-sell/upsell) to increase repeat purchase rates.

Prioritize high-LTV segments for richer personalization.

Loyalty program design

Pilot a points-based loyalty program for frequent buyers; test its effect on repeat purchase frequency.

Fulfillment & returns optimization

If delivery problems are identified in surveys/cohorts, fix logistics bottlenecks.

C. Long term (9–18 months) — "Sustain & Scale"

Product roadmap alignment

Incorporate retention KPIs into product goals (e.g., reduce friction, improve discoverability).

Measurement & experimentation infrastructure

Build (or expand) experimentation to measure retention impact (longer A/B tests, holdouts).

Customer success & lifecycle marketing

Invest in lifecycle orchestration — triggered emails, lifecycle journeys, and lifecycle analysts.

Recommended short experiments (to test quickly)

Experiment 1 — Onboarding email sequence A/B test
Hypothesis: A 5-email onboarding sequence with product tips increases 90-day retention by 1.5 pp for new customers.

Experiment 2 — Winback creative & offer test
Hypothesis: A personalized product-based win-back achieves 10% reactivation at acceptable CPA compared to generic discount.

Experiment 3 — Loyalty pilot
Hypothesis: Early adopters of a loyalty program increase repeat purchase frequency by 8% over 6 months.

Simple projection examples

If the company can improve average retention by:

+0.5 percentage points per quarter → ~26 quarters to close the 12.9 pp gap (illustrative)

+1.0 percentage point per quarter → ~13 quarters

+2.0 percentage points per quarter → ~7 quarters

(These projections are linear and illustrative. Real improvements compound and require cohort-level tracking.)

Next steps & deliverables for management

Run cohort analysis (channel / product / geography) to find where churn is concentrated.

Instrument surveys for Q2 & Q3 churned customers and analyze qualitative feedback.

Run the top 2 experiments (onboarding A/B and winback pilot) and measure lift in 30/90/180-day retention.

Prepare a 6-month retention playbook based on experiment results and roll out the loyalty pilot.

Reproducibility

Run:

pip install -r requirements.txt
python3 analysis/analysis.py


This will produce visuals/retention_trend.png and analysis/analysis_summary.txt.

Contact / verification

24f2009283@ds.study.iitm.ac.in


---

