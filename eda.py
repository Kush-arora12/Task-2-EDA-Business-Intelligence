import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================
# Load Dataset
# ============================

df = pd.read_excel("Cleaned_Sales_Dataset_SQL.csv")

# ============================
# Dataset Information
# ============================

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)
print(df.info())

print("\n")

# ============================
# Descriptive Statistics
# ============================

print("=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)
print(df.describe(include='all'))

print("\n")

# ============================
# Missing Values
# ============================

print("=" * 60)
print("MISSING VALUES")
print("=" * 60)
print(df.isnull().sum())

print("\n")

# ============================
# Histograms
# ============================

numerical_cols = ['Age', 'Quantity', 'Unit_Price', 'Total_Sales']

for col in numerical_cols:
    plt.figure(figsize=(7,5))
    plt.hist(df[col], bins=15, edgecolor='black')
    plt.title(f'{col} Distribution')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    plt.savefig(f"{col}_Histogram.png", dpi=300, bbox_inches='tight')
    plt.show()

# ============================
# Bar Charts
# ============================

categorical_cols = ['Gender', 'Category', 'City']

for col in categorical_cols:
    plt.figure(figsize=(8,5))
    df[col].value_counts().plot(kind='bar')

    plt.title(f'{col} Distribution')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    plt.savefig(f"{col}_BarChart.png", dpi=300, bbox_inches='tight')
    plt.show()

# ============================
# Scatter Plot
# ============================

plt.figure(figsize=(8,5))
plt.scatter(df['Age'], df['Total_Sales'], alpha=0.6)

plt.title("Age vs Total Sales")
plt.xlabel("Age")
plt.ylabel("Total Sales")

plt.savefig("Age_vs_TotalSales_Scatter.png", dpi=300, bbox_inches='tight')
plt.show()

# ============================
# Correlation Heatmap
# ============================

plt.figure(figsize=(6,5))

corr = df[['Age','Quantity','Unit_Price','Total_Sales']].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Correlation Heatmap")

plt.savefig("Correlation_Heatmap.png", dpi=300, bbox_inches='tight')
plt.show()

# ============================
# Pair Plot
# ============================

pair = sns.pairplot(
    df[['Age','Quantity','Unit_Price','Total_Sales']]
)

pair.savefig("PairPlot.png", dpi=300)

plt.show()

# ============================
# Value Counts
# ============================

print("=" * 60)
print("VALUE COUNTS")
print("=" * 60)

for col in categorical_cols:
    print(f"\n{col}")
    print(df[col].value_counts())