
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# 1. Project setup
OUTPUT_DIR = Path("charts")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv("hr_data.csv")

# 2. Validate the dataset
required_columns = [
    "Attrition",
    "JobRole",
    "OverTime",
    "MonthlyIncome",
    "JobSatisfaction",
]

missing_columns = set(required_columns) - set(df.columns)

if missing_columns:
    raise ValueError(f"Missing columns: {missing_columns}")

print("=" * 50)
print("HR EMPLOYEE ATTRITION ANALYSIS")
print("=" * 50)

print(f"Total employees: {len(df)}")
print(f"Missing values: {df.isnull().sum().sum()}")

# 3. Overall attrition KPIs
total_employees = len(df)
employees_left = (df["Attrition"] == "Yes").sum()
overall_rate = (employees_left / total_employees) * 100

print(f"Employees who left: {employees_left}")
print(f"Overall attrition rate: {overall_rate:.2f}%")

# 4. Attrition by job role
role_summary = df.groupby("JobRole").agg(
    employees=("Attrition", "size"),
    left=("Attrition", lambda x: (x == "Yes").sum()),
    attrition_rate=(
        "Attrition",
        lambda x: (x == "Yes").mean() * 100
    ),
)

role_summary = role_summary.sort_values(
    "attrition_rate", ascending=False
)

print("\nATTRITION BY JOB ROLE")
print(role_summary.round(2))

role_summary.to_csv("role_summary.csv")

ax = role_summary["attrition_rate"].sort_values().plot(
    kind="barh", figsize=(9, 6)
)
ax.set_title("Employee Attrition Rate by Job Role")
ax.set_xlabel("Attrition Rate (%)")
ax.set_ylabel("Job Role")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "attrition_by_role.png", dpi=300)
plt.close()

# 5. Attrition by overtime
overtime_summary = df.groupby("OverTime").agg(
    employees=("Attrition", "size"),
    left=("Attrition", lambda x: (x == "Yes").sum()),
    attrition_rate=(
        "Attrition",
        lambda x: (x == "Yes").mean() * 100
    ),
)

print("\nATTRITION BY OVERTIME")
print(overtime_summary.round(2))

overtime_summary.to_csv("overtime_summary.csv")

ax = overtime_summary["attrition_rate"].plot(
    kind="bar", figsize=(7, 5)
)
ax.set_title("Employee Attrition by Overtime")
ax.set_xlabel("Works Overtime")
ax.set_ylabel("Attrition Rate (%)")
ax.tick_params(axis="x", rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "attrition_by_overtime.png", dpi=300)
plt.close()

# 6. Attrition by job satisfaction and overtime
satisfaction_overtime = df.groupby(
    ["JobSatisfaction", "OverTime"]
).agg(
    employees=("Attrition", "size"),
    left=("Attrition", lambda x: (x == "Yes").sum()),
    attrition_rate=(
        "Attrition",
        lambda x: (x == "Yes").mean() * 100
    ),
)

print("\nATTRITION BY SATISFACTION AND OVERTIME")
print(satisfaction_overtime.round(2))

satisfaction_overtime.to_csv(
    "satisfaction_overtime_summary.csv"
)

chart_data = satisfaction_overtime[
    "attrition_rate"
].unstack("OverTime")

ax = chart_data.plot(kind="bar", figsize=(9, 5))
ax.set_title("Attrition by Satisfaction and Overtime")
ax.set_xlabel("Job Satisfaction (1 = Low, 4 = High)")
ax.set_ylabel("Attrition Rate (%)")
ax.tick_params(axis="x", rotation=0)
ax.legend(title="Works Overtime")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "attrition_satisfaction_overtime.png",
    dpi=300
)
plt.close()

# 7. Attrition by monthly income group
df["IncomeGroup"] = pd.qcut(
    df["MonthlyIncome"],
    q=4,
    labels=["Low", "Medium-Low", "Medium-High", "High"]
)

income_summary = df.groupby(
    "IncomeGroup", observed=True
).agg(
    employees=("Attrition", "size"),
    left=("Attrition", lambda x: (x == "Yes").sum()),
    attrition_rate=(
        "Attrition",
        lambda x: (x == "Yes").mean() * 100
    ),
)

print("\nATTRITION BY INCOME GROUP")
print(income_summary.round(2))

income_summary.to_csv("income_summary.csv")

ax = income_summary["attrition_rate"].plot(
    kind="bar", figsize=(8, 5)
)
ax.set_title("Employee Attrition by Monthly Income")
ax.set_xlabel("Income Group")
ax.set_ylabel("Attrition Rate (%)")
ax.tick_params(axis="x", rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "attrition_by_income.png", dpi=300)
plt.close()

print("\nAnalysis complete!")
print(f"Charts saved in: {OUTPUT_DIR.resolve()}")
print("Summary CSV files saved in the project folder.")
