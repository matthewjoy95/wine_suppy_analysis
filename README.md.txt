# U.S. Wine Trends (TTB Monthly Report)

This project analyzes U.S. wine production and category trends using monthly data from the Alcohol and Tobacco Tax and Trade Bureau (TTB).

## Objective
Identify short-term demand and production patterns across major wine categories:
- Still wine (≤16% ABV)
- Sparkling wine
- Total production

## Tools Used
- Python (pandas, matplotlib)
- Excel data (TTB monthly reports)

## How to Run

```bash
pip install pandas matplotlib openpyxl
python3 wine_trends.py
```

## Output

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
