# U.S. Wine Trends (TTB Monthly Report)

This project analyzes U.S. wine production and category trends using monthly data from the Alcohol and Tobacco Tax and Trade Bureau (TTB).

## Objective
Identify short-term demand and production patterns across major wine categories:
- Still wine (≤16% ABV)
- Sparkling wine
- Total production

## Key Insight

Wine production in 2025 shows a clear seasonal pattern:

- Steady decline from January through mid-year (July)
- Sharp increase beginning in late summer (August–October)

This pattern suggests strong alignment with harvest cycles and highlights the importance of seasonality in production planning and inventory forecasting.

## Process

- Cleaned raw Excel data with non-standard headers and formatting
- Selected relevant production metrics
- Converted wide monthly data into long format for analysis
- Constructed a time-based index for trend analysis
- Applied a 3-month rolling average to reduce noise
- Visualized production and category trends

## Tools Used
- Python (pandas, matplotlib)
- Excel data (TTB monthly reports)

## How to Run

```bash
pip install pandas matplotlib openpyxl
python3 wine_trends.py
```

## Output

![Wine Trends](outputs/wine_trends_2025.png)

The script produces a smoothed trend chart saved to:

```
outputs/wine_trends_2025.png
```

## Notes

This is a portfolio project demonstrating:
- Real-world Excel data cleaning
- Wide-to-long reshaping
- Time series visualization
- Reproducible analysis workflow
