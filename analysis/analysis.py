"""
analysis/analysis.py

Run:
    python3 analysis.py

This script:
 - Loads the quarterly retention data
 - Computes summary stats (average shown as 72.1 in README)
 - Plots the quarterly trend and industry benchmark line and saves to ../visuals/retention_trend.png
 - Prints a short summary to stdout
"""

import os
from pathlib import Path
import math

import matplotlib.pyplot as plt

# Data (Customer Retention Rate - 2024 Quarterly Data)
quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
values = [71.14, 69.47, 71.89, 75.91]

# Benchmarks & constants
industry_benchmark = 85.0

# Ensure output dir exists
out_dir = Path(__file__).resolve().parents[1] / "visuals"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "retention_trend.png"

# Summary stats
n = len(values)
_sum = sum(values)
_avg = _sum / n
# For README we present rounded average 72.1 (as required). We'll compute precise but format to 1 decimal.
avg_rounded = round(_avg, 1)  # 72.1

# Print quick summary
print("Quarterly retention values:", values)
print(f"Computed average: {_avg:.4f}")
print(f"Rounded average (for report): {avg_rounded}")

# Basic trend plot
plt.figure(figsize=(9, 5))
plt.plot(quarters, values, marker='o', linewidth=2)
plt.axhline(industry_benchmark, linestyle='--', linewidth=1.5, label=f"Industry target = {industry_benchmark}")
plt.title("Customer Retention Rate — 2024 Quarterly Trend")
plt.ylabel("Retention Rate (%)")
plt.ylim(min(min(values) - 5, 0), max(industry_benchmark + 5, max(values) + 5))
plt.grid(axis='y', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(out_path, dpi=150)
plt.close()

print(f"Saved retention trend chart to: {out_path}")

# Simple linear improvement projection (illustrative only)
# If we implemented initiatives that increase retention by a fixed percentage points per quarter,
# estimate how many quarters needed to reach benchmark.
current = _avg
gap = industry_benchmark - current
print(f"Current average retention: {current:.4f} (gap to benchmark: {gap:.4f} percentage points)")

# Example: if targeted campaigns can improve retention by X percentage points per quarter:
for improvement_per_q in [0.5, 1.0, 2.0]:  # in percentage points per quarter
    if improvement_per_q <= 0:
        continue
    quarters_needed = math.ceil(gap / improvement_per_q)
    print(f"At +{improvement_per_q:.1f} pp per quarter, estimated quarters to reach {industry_benchmark}: {quarters_needed}")

# Save a short text summary
summary_txt = out_dir.parent / "analysis_summary.txt"
with open(summary_txt, "w") as f:
    f.write("E-commerce retention analysis summary\n")
    f.write(f"Quarterly values: {values}\n")
    f.write(f"Computed average: {_avg:.4f}\n")
    f.write(f"Reported average (rounded): {avg_rounded}\n")
    f.write(f"Industry benchmark: {industry_benchmark}\n")
    f.write(f"Gap to benchmark: {gap:.4f}\n")
    f.write("Projection examples (quarters to reach target) for improvements of 0.5, 1.0, 2.0 pp/qtr included.\n")

print(f"Wrote short summary to: {summary_txt}")
