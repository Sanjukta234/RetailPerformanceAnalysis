📊 Retail Performance Analysis – Inventory Turnover (2024)

Author: 22f1001636@ds.study.iitm.ac.in

Summary

This PR adds a complete data analysis package for the company’s 2024 Inventory Turnover Ratio, benchmarking performance against the industry target of 8. It includes Python analysis code, dataset, visualizations, and a comprehensive data story in the README.md.

Key Findings

Average turnover (2024): 4.88, below the industry benchmark of 8.

Volatility observed: Q1 anomaly (-0.68), Q2 peak (8.04), Q3 dip (4.28), Q4 recovery (7.88).

Indicates excess inventory, capital lock-up, and higher carrying/storage costs.

Short-lived recoveries suggest gaps in forecast accuracy and inventory management.

Business Implications

Capital tie-up in slow-moving SKUs, limiting financial flexibility.

Higher operational/storage costs and increased risk of obsolescence.

Forecasting challenges leading to mismatched supply vs. demand.

Recommendations

Solution theme: Optimize supply chain and demand forecasting

Enhance demand forecasting (hierarchical models, external drivers, weekly re-forecasting).

Optimize inventory policies (safety stock, reorder points, SKU rationalization).

Strengthen supply chain execution (supplier lead-time reduction, MEIO, cycle counting).

Align promotion & pricing with supply-demand signals.

Improve governance (dashboards, KPIs, incentive alignment).

Files Added

analysis.py – Python code to process data and generate plots.

inventory_turnover_2024.csv – Quarterly dataset.

turnover_trend.png – Line chart vs. target.

turnover_bars.png – Bar chart vs. target.

README.md – Comprehensive data story.

Evidence of LLM Assistance


