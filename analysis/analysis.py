"""
analysis.py
Performs quarterly retention rate analysis, computes summary statistics,
creates a trend visualization, and saves chart output.

Author: 24f2009283@ds.study.iitm.ac.in
Generated with assistance from ChatGPT Codex (Jules)
https://chatgpt.com/codex/tasks
"""

import matplotlib.pyplot as plt
from pathlib import Path

# Quarterly Retention Data (2024)
quarters = ["Q1", "Q2", "Q3", "Q4"]
values = [71.14, 69.47, 71.89, 75.91]

# Industry Benchmark
benchmark = 85

# Compute Average
average_retention = round(sum(values) / len(values), 1)  # 72.1

print(f"Quarterly values: {values}")
print(f"Computed average retention (reported): {average_retention}")

# Create visuals directory if not exists
output_dir = Path("visuals")
output_dir.mkdir(exist_ok=True)

# Plot retention trend
plt.figure(figsize=(8, 5))
plt.plot(quarters, values, marker='o', linewidth=2)
plt.axhline(benchmark, ls='--', label=f"Benchmark = {benchmark}")
plt.title("Customer Retention Rate – 2024 Quarterly Trend")
plt.xlabel("Quarter")
plt.ylabel("Retention (%)")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

# Save plot
chart_path = output_dir / "retention_trend.png"
plt.savefig(chart_path, dpi=150)
plt.close()

print(f"Chart saved to: {chart_path}")
