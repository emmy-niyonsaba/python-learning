"""
Module     : Python and Fundamentals of Artificial Intelligence
Student    : Emmanuel Niyonsaba
RegNumber: 24rp04021
Dataset    : Titanic passenger dataset (891 rows, 15 columns)


"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, PatternFill

BASE = Path(__file__).resolve().parent
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)


def title(text):
    print("\n" + "=" * 80)
    print(text)
    print("=" * 80)


# =============================================================================
# PART A - DATASET SELECTION AND IMPORTATION
# =============================================================================
title("QUESTION 1: DATASET INFORMATION")
print("""Dataset : Titanic passenger data (real passenger records, RMS Titanic, 1912)
Source  : Kaggle 'Titanic - Machine Learning from Disaster'; downloaded as CSV from
          the seaborn-data repository (github.com/mwaskom/seaborn-data)
Purpose : Study which passenger characteristics were associated with survival.
Size    : 891 rows x 15 columns (numerical + categorical data)

Meaning of key columns:
  survived    - 1 = passenger survived, 0 = did not survive
  pclass      - ticket class (1 = First, 2 = Second, 3 = Third)
  sex         - passenger gender (male / female)
  age         - age in years (fractions for infants)
  sibsp       - number of siblings / spouses aboard
  parch       - number of parents / children aboard
  fare        - ticket price paid (pounds sterling)
  embark_town - port of embarkation (Southampton, Cherbourg, Queenstown)
  deck        - cabin deck letter (A-G)
""")

title("QUESTION 2: IMPORTATION AND EXPLORATION")
# 2a. Import
df = pd.read_csv(BASE / "titanic_original.csv")
raw = df.copy()  # untouched copy of the original data

# 2b. First 10 and last 10 records
print("First 10 records:")
print(df.head(10))
print("\nLast 10 records:")
print(df.tail(10))

# 2c. Rows and columns
print(f"\nNumber of rows   : {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")

# 2d. Column names and data types
print("\nColumn names:", list(df.columns))
print("\nData types:")
print(df.dtypes)

# 2e. info() and describe()
print("\ndf.info():")
df.info()
print("\ndf.describe() (numerical columns):")
print(df.describe())
print("\ndf.describe(include='object') (categorical columns):")
print(df.describe(include=["object", "string"]))

# =============================================================================
# PART B - DATA SELECTION AND FILTERING (done on the original data)
# =============================================================================
title("QUESTION 3: SELECTING AND FILTERING RECORDS")

# 3a. Three relevant columns
print("3a. Selected columns: sex, age, survived (first 5 rows)")
print(df[["sex", "age", "survived"]].head())
print("Why: these are the core variables for studying who survived.")

# 3b. Numerical condition
older = df[df["age"] > 60]
print(f"\n3b. Passengers older than 60: {len(older)} records")
print(older[["sex", "age", "pclass", "survived"]].head())
print("Why: shows how few elderly passengers there were and lets us inspect their survival.")

# 3c. Categorical condition
females = df[df["sex"] == "female"]
print(f"\n3c. Female passengers: {len(females)} records")
print("Why: lets us compare the group with the male passengers on survival.")

# 3d. Multiple conditions with & and |
first_female = df[(df["pclass"] == 1) & (df["sex"] == "female")]
print(f"\n3d-i. First-class AND female: {len(first_female)} records, "
      f"survival rate = {first_female['survived'].mean():.2%}")
kids_or_old = df[(df["age"] < 12) | (df["age"] > 60)]
print(f"3d-ii. Age < 12 OR age > 60: {len(kids_or_old)} records, "
      f"survival rate = {kids_or_old['survived'].mean():.2%}")
print("Why: combined conditions isolate specific passenger profiles.")

# 3e. Sorting
top_fares = df.sort_values("fare", ascending=False)
print("\n3e. Top 10 passengers by fare paid (descending):")
print(top_fares[["pclass", "sex", "age", "fare", "survived"]].head(10))
print("Why: sorting by fare shows the wealthiest passengers and their outcomes.")

# =============================================================================
# PART C - DATA CLEANING AND PREPARATION
# =============================================================================
title("QUESTION 4: MISSING VALUES")

# 4a. Count missing values
missing_count = df.isnull().sum()
print("4a. Missing values per column:")
print(missing_count)

# 4b. Percentages
missing_pct = (df.isnull().mean() * 100).round(2)
print("\n4b. Missing percentage per column:")
print(missing_pct)

# 4c. Handling methods
print("\n4c. Handling missing values")

# Method 1 - drop the column: 'deck' is ~77% empty, so imputing it would
# mostly invent data.
df = df.drop(columns=["deck"])
print("Method 1: dropped column 'deck' (77.2% missing).")

# Method 2 - median imputation: 'age' is numerical and skewed, so the median
# is robust. We use the median of the passenger's own class and sex because
# age differs by class (first-class passengers were older on average).
# A flag column keeps track of which ages were estimated.
df["age_imputed"] = df["age"].isnull()
df["age"] = df["age"].fillna(df.groupby(["pclass", "sex"])["age"].transform("median"))
print(f"Method 2: filled {int(df['age_imputed'].sum())} missing ages with the "
      "median age of the same class and sex.")

# Method 3 - mode imputation: 'embark_town' and 'embarked' are categorical
# and only 2 values are missing, so the most frequent value is the safest.
mode_town = df["embark_town"].mode()[0]
mode_port = df["embarked"].mode()[0]
df["embark_town"] = df["embark_town"].fillna(mode_town)
df["embarked"] = df["embarked"].fillna(mode_port)
print(f"Method 3: filled 2 missing embarkation values with the mode ('{mode_town}').")

print("\nMissing values after handling:")
print(df.isnull().sum())

# 4d. Justification
print("""
4d. Why these methods?
  - Dropping 'deck': with 77% missing, any imputation would be mostly guesswork.
  - Median for 'age': the median is not distorted by very old/young outliers, and
    grouping by class and sex gives a more realistic estimate than one global value.
    Deleting the 177 rows (19.9%) would have thrown away too much useful data.
  - Mode for embarkation: categorical data has no median/mean; the mode is the most
    probable value and only 0.2% of rows are affected.""")

title("QUESTION 5: DUPLICATE AND INCORRECT RECORDS")

# 5a. Identify duplicates
dup_count = int(df.duplicated().sum())
print(f"5a. Duplicate records found: {dup_count}")
print(df[df.duplicated(keep=False)].sort_values(list(df.columns)).head(10))

# 5b. Remove duplicates
before = len(df)
df = df.drop_duplicates().reset_index(drop=True)
print(f"\n5b. Removed {before - len(df)} duplicates. Rows: {before} -> {len(df)}")
print("Note: the dataset has no passenger-ID column, so rows identical in every "
      "field are treated as duplicate entries.")

# 5c. Invalid / inconsistent values
print("\n5c. Checking for invalid or inconsistent values")
zero_fare = df[df["fare"] == 0]
print(f"  - Records with fare = 0: {len(zero_fare)}")
print(f"  - Negative ages: {(df['age'] < 0).sum()}, ages above 100: {(df['age'] > 100).sum()}")
print(f"  - Negative sibsp/parch: {((df['sibsp'] < 0) | (df['parch'] < 0)).sum()}")
print(f"  - 'survived' vs 'alive' mismatches: "
      f"{(df['survived'] != (df['alive'] == 'yes').astype(int)).sum()}")
print(f"  - 'pclass' vs 'class' mismatches: "
      f"{(df['pclass'] != df['class'].map({'First': 1, 'Second': 2, 'Third': 3})).sum()}")
print(f"  - 'alone' flag vs sibsp+parch mismatches: "
      f"{(df['alone'] != ((df['sibsp'] + df['parch']) == 0)).sum()}")
print("  - Inconsistent category spelling:")
for col in ["sex", "embark_town", "class", "who", "alive"]:
    print(f"      {col}: {sorted(df[col].unique())}")

# 5d. Correct or remove
print("\n5d. Corrections")
# A ticket fare of 0 is not a realistic price for a ticket in 1st/2nd/3rd class;
# it is treated as a missing value and replaced with the median fare of the
# passenger's class.
df["fare"] = df["fare"].mask(df["fare"] == 0)
df["fare"] = df["fare"].fillna(df.groupby("pclass")["fare"].transform("median"))
print(f"  - Replaced {len(zero_fare)} zero fares with the median fare of the same class.")

# 'alive', 'class' and 'embarked' were verified to be exact copies of
# 'survived', 'pclass' and 'embark_town' (0 mismatches), so they add no
# information and are removed to avoid redundancy.
df = df.drop(columns=["alive", "class", "embarked"])
print("  - Dropped redundant columns 'alive', 'class', 'embarked' (verified identical to "
      "'survived', 'pclass', 'embark_town').")
print("  - No negative/impossible ages or counts were found, so no records were removed.")

title("QUESTION 6: DATA TRANSFORMATION")

# 6a. Data types
df["survived"] = df["survived"].astype("int8")
df["sibsp"] = df["sibsp"].astype("int8")
df["parch"] = df["parch"].astype("int8")
df["pclass"] = pd.Categorical(df["pclass"], categories=[1, 2, 3], ordered=True)
print("6a. Converted: survived/sibsp/parch -> int8; pclass -> ordered category.")

# 6b. Standardise text
text_cols = ["sex", "who", "embark_town"]
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()
    df[col] = df[col].astype("category")
print("6b. Text columns stripped of spaces, converted to Title Case and set to "
      "category type:", text_cols)

# 6c. Rename columns
df = df.rename(columns={
    "pclass": "passenger_class",
    "sibsp": "siblings_spouses_aboard",
    "parch": "parents_children_aboard",
    "embark_town": "port_of_embarkation",
    "fare": "ticket_fare_gbp",
    "who": "passenger_type",
    "alone": "travelling_alone",
})
print("6c. Renamed: pclass, sibsp, parch, embark_town, fare, who, alone.")

# 6d. Calculated columns
df["family_size"] = df["siblings_spouses_aboard"] + df["parents_children_aboard"] + 1
df["age_group"] = pd.cut(
    df["age"], bins=[0, 12, 19, 59, 120],
    labels=["Child", "Teenager", "Adult", "Senior"], right=True,
)
df["fare_per_person_gbp"] = (df["ticket_fare_gbp"] / df["family_size"]).round(2)
df["survival_status"] = df["survived"].map({1: "Survived", 0: "Did Not Survive"})
print("6d. Created: family_size, age_group, fare_per_person_gbp, survival_status.")

print("\nCleaned dataset preview:")
print(df.head(10))
print("\nFinal data types:")
print(df.dtypes)
print(f"\nFinal shape: {df.shape}")

# =============================================================================
# PART D - STATISTICAL ANALYSIS AND GROUPING (cleaned dataset only)
# =============================================================================
title("QUESTION 7: STATISTICAL CALCULATIONS")
num_cols = ["age", "ticket_fare_gbp", "family_size"]

stats = pd.DataFrame({
    "Mean": df[num_cols].mean(),
    "Median": df[num_cols].median(),
    "Minimum": df[num_cols].min(),
    "Maximum": df[num_cols].max(),
    "Std Deviation": df[num_cols].std(),
}).round(2)
print("7a-c. Mean, median, min, max, std:")
print(stats)

# 7d. Highest / lowest
mean_fare_class = df.groupby("passenger_class", observed=True)["ticket_fare_gbp"].mean()
top_class = mean_fare_class.idxmax()
print(f"\n7d. Highest average fare: class {top_class} (GBP {mean_fare_class.max():.2f}); "
      f"lowest: class {mean_fare_class.idxmin()} (GBP {mean_fare_class.min():.2f}).")
surv_by_class = df.groupby("passenger_class", observed=True)["survived"].mean()
print(f"    Highest survival rate: class {surv_by_class.idxmax()} "
      f"({surv_by_class.max():.1%}); lowest: class {surv_by_class.idxmin()} "
      f"({surv_by_class.min():.1%}).")
print("    Interpretation: first-class passengers paid far more and also survived "
      "most often, so ticket class is strongly linked to survival.")

title("QUESTION 8: GROUPING AND SUMMARIZING DATA")

# 8a. Group and count
sex_counts = df.groupby("sex", observed=True).size().rename("Passengers")
print("8a. Passengers per sex:")
print(sex_counts)
class_counts = df.groupby("passenger_class", observed=True).size().rename("Passengers")
print("\nPassengers per class:")
print(class_counts)

# 8b. Mean per group
print("\n8b. Mean age by passenger class:")
print(df.groupby("passenger_class", observed=True)["age"].mean().round(2))
print("\nMean survival rate by sex:")
print(df.groupby("sex", observed=True)["survived"].mean().round(4))

# 8c. groupby + agg
class_summary = df.groupby("passenger_class", observed=True).agg(
    passengers=("survived", "count"),
    survivors=("survived", "sum"),
    survival_rate=("survived", "mean"),
    mean_age=("age", "mean"),
    median_age=("age", "median"),
    mean_fare=("ticket_fare_gbp", "mean"),
    max_fare=("ticket_fare_gbp", "max"),
    std_fare=("ticket_fare_gbp", "std"),
).round(3)
print("\n8c. Summary by passenger class (groupby + agg):")
print(class_summary)

sex_summary = df.groupby("sex", observed=True).agg(
    passengers=("survived", "count"),
    survivors=("survived", "sum"),
    survival_rate=("survived", "mean"),
    mean_age=("age", "mean"),
    mean_fare=("ticket_fare_gbp", "mean"),
).round(3)

port_summary = df.groupby("port_of_embarkation", observed=True).agg(
    passengers=("survived", "count"),
    survival_rate=("survived", "mean"),
    mean_fare=("ticket_fare_gbp", "mean"),
    median_age=("age", "median"),
).round(3)

age_summary = df.groupby("age_group", observed=True).agg(
    passengers=("survived", "count"),
    survival_rate=("survived", "mean"),
    mean_fare=("ticket_fare_gbp", "mean"),
).round(3)

class_sex = df.pivot_table(index="passenger_class", columns="sex",
                           values="survived", aggfunc="mean", observed=True).round(3)

# 8d. Sort and identify highest
sorted_ports = port_summary.sort_values("passengers", ascending=False)
print("\n8d. Ports sorted by number of passengers:")
print(sorted_ports)
print(f"Largest group: {sorted_ports.index[0]} ({sorted_ports['passengers'].iloc[0]} passengers)")
best_group = class_summary.sort_values("survival_rate", ascending=False)
print(f"Highest-performing class (survival): class {best_group.index[0]} "
      f"({best_group['survival_rate'].iloc[0]:.1%})")

# 8e. Interpretation
f_rate = sex_summary.loc["Female", "survival_rate"]
m_rate = sex_summary.loc["Male", "survival_rate"]
c1 = class_summary.loc[1, "survival_rate"]
c3 = class_summary.loc[3, "survival_rate"]
child_rate = age_summary.loc["Child", "survival_rate"]
adult_rate = age_summary.loc["Adult", "survival_rate"]
print(f"""
8e. Findings
  1. Gender: females survived at {f_rate:.1%} versus {m_rate:.1%} for males.
  2. Class: first class survival was {c1:.1%} versus {c3:.1%} in third class.
  3. Age: children (<=12) survived at {child_rate:.1%} versus {adult_rate:.1%} for adults.""")

# =============================================================================
# PART E - SAVING AND REPORTING
# =============================================================================
title("QUESTION 9: EXPORTING PROCESSED DATA")

# 9a. Cleaned dataset
df.to_csv(BASE / "cleaned_dataset.csv", index=False)
print("9a. Saved cleaned_dataset.csv")

# 9b. Summary workbook
overall = stats.reset_index().rename(columns={"index": "Variable"})
with pd.ExcelWriter(BASE / "summary_report.xlsx", engine="openpyxl") as writer:
    overall.to_excel(writer, sheet_name="Overall_Statistics", index=False)
    class_summary.reset_index().to_excel(writer, sheet_name="By_Class", index=False)
    sex_summary.reset_index().to_excel(writer, sheet_name="By_Sex", index=False)
    port_summary.reset_index().to_excel(writer, sheet_name="By_Port", index=False)
    age_summary.reset_index().to_excel(writer, sheet_name="By_AgeGroup", index=False)
    class_sex.reset_index().to_excel(writer, sheet_name="Survival_Class_x_Sex", index=False)

# Formatting
wb = load_workbook(BASE / "summary_report.xlsx")
for ws in wb.worksheets:
    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="1F4E78")
        cell.alignment = Alignment(horizontal="center")
    for col in ws.columns:
        width = max(len(str(c.value)) if c.value is not None else 0 for c in col)
        ws.column_dimensions[col[0].column_letter].width = max(width + 4, 14)
wb.save(BASE / "summary_report.xlsx")
print("9b. Saved summary_report.xlsx (6 sheets)")

# 9c. Verify
check_csv = pd.read_csv(BASE / "cleaned_dataset.csv")
check_xlsx = pd.read_excel(BASE / "summary_report.xlsx", sheet_name=None)
print(f"9c. cleaned_dataset.csv re-opened: {check_csv.shape[0]} rows x "
      f"{check_csv.shape[1]} columns; missing values = {int(check_csv.isnull().sum().sum())}")
for name, sheet in check_xlsx.items():
    print(f"    summary_report.xlsx -> sheet '{name}': {sheet.shape[0]} rows x {sheet.shape[1]} columns")

# Charts used in the report
fig, ax = plt.subplots(1, 3, figsize=(13, 4))
(sex_summary["survival_rate"] * 100).plot(kind="bar", ax=ax[0], color=["#C0504D", "#1F4E78"])
ax[0].set_title("Survival rate by sex (%)")
(class_summary["survival_rate"] * 100).plot(kind="bar", ax=ax[1], color="#1F4E78")
ax[1].set_title("Survival rate by class (%)")
(age_summary["survival_rate"] * 100).plot(kind="bar", ax=ax[2], color="#4F81BD")
ax[2].set_title("Survival rate by age group (%)")
for a in ax:
    a.set_xlabel("")
    a.tick_params(axis="x", rotation=0)
    a.set_ylim(0, 100)
plt.tight_layout()
plt.savefig(BASE / "analysis_charts.png", dpi=150)
print("Saved analysis_charts.png")

title("PROGRAM COMPLETED SUCCESSFULLY")
