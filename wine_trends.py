import pandas as pd
import matplotlib.pyplot as plt

FILE = "data/Wine_National_Report.xlsx"
SHEET = "2025"          # keep it simple for now
SKIPROWS = 7            # works for the top table in your screenshot

# Load one year
df = pd.read_excel(FILE, sheet_name=SHEET, skiprows=SKIPROWS)

# First col is the metric names
df = df.rename(columns={df.columns[0]: "Metric"})
df = df.dropna(subset=["Metric"]).copy()

# Keep only the rows we care about (top table metrics)
keep = {
    "Still Wine ≤ 16% ABV",
    "Sparkling Wine",
    "Production",
}
df = df[df["Metric"].astype(str).str.strip().isin(keep)]

# Identify month columns (handles "January 2025", "January\n2025", etc.)
month_names = ["january","february","march","april","may","june","july","august","september","october","november","december"]
month_cols = [c for c in df.columns if any(m in str(c).strip().lower() for m in month_names)]

# Convert wide -> long
long = df.melt(id_vars="Metric", value_vars=month_cols, var_name="MonthCol", value_name="Gallons")
long["Gallons"] = pd.to_numeric(long["Gallons"], errors="coerce")
long = long.dropna(subset=["Gallons"])

# Extract month name from column header, then build dates
long["Month"] = long["MonthCol"].astype(str).str.strip().str.split().str[0].str.lower()
month_map = {m: i+1 for i, m in enumerate(month_names)}
long["MonthNum"] = long["Month"].map(month_map)
long = long.dropna(subset=["MonthNum"])

long["Date"] = pd.to_datetime(
    {"year": int(SHEET), "month": long["MonthNum"].astype(int), "day": 1},
    errors="coerce"
)
long = long.dropna(subset=["Date"]).sort_values("Date")

# Pivot for plotting
wide = long.pivot_table(index="Date", columns="Metric", values="Gallons", aggfunc="sum").sort_index()

# 3-month smoothing (looks nicer with monthly noise)
smooth = wide.rolling(3, min_periods=1).mean()

plt.figure(figsize=(10,6))
for col in smooth.columns:
    plt.plot(smooth.index, smooth[col], label=col)

plt.title("U.S. Wine Indicators (TTB Monthly Report, 2025) — 3-mo Avg")
plt.xlabel("Month")
plt.ylabel("Gallons")
plt.legend()
plt.tight_layout()

# Save output for GitHub
plt.savefig("wine_trends_2025.png", dpi=200)
plt.show()

print("Saved chart: wine_trends_2025.png")
print("Rows:", len(long), "| Date range:", long["Date"].min().date(), "to", long["Date"].max().date())
print("Metrics plotted:", list(wide.columns))
