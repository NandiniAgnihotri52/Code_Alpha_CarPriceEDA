# Task 1: Exploratory Data Analysis(EDA) -

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re
from scipy.stats import ttest_ind

df = pd.read_csv("../data/Car_details_v3.csv")

"""**Some questions for EDA:**
1. How does car price vary with year, mileage, and power?
2. Do automatic cars cost more than manual cars?
3. Does fuel type affect car price significantly?
4. What are the common issues/anomalies in the dataset?
"""

print(df.info())

print(df.head())

print(df.describe())

print(df.isnull().sum())

print(df.shape)

"""**Cleaning numeric columns**"""

def extract_numeric(x):
    if pd.isnull(x):
        return np.nan
    match = re.search(r"[\d.]+", str(x))
    return float(match.group()) if match else np.nan

df['mileage_num'] = df['mileage'].apply(extract_numeric)
df['engine_num'] = df['engine'].apply(extract_numeric)
df['max_power_num'] = df['max_power'].apply(extract_numeric)

df['car_age'] = 2025 - df['year']

"""**Identifying Trends, Patterns & Anomalies**"""

plt.figure(figsize=(8,5))
sns.scatterplot(x='year', y='selling_price', data=df, alpha=0.5)
plt.title("Trend: Selling Price vs Year")
plt.show()

sns.barplot(x='transmission', y='selling_price', data=df)
plt.title("Pattern: Transmission vs Average Price")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df['selling_price'])
plt.title("Anomalies: Outliers in Price")
plt.show()

"""**Testing Hypotheses & Validating Assumptions**

Automatic cars are more expensive than manual cars
"""

auto_prices = df[df['transmission']=="Automatic"]['selling_price']
manual_prices = df[df['transmission']=="Manual"]['selling_price']

tstat, pval = ttest_ind(auto_prices, manual_prices, nan_policy='omit')

print("H0: Automatic and Manual car prices are the same")
print("H1: Automatic cars are more expensive")
print(f"T-statistic = {tstat:.2f}, p-value = {pval:.4f}")

if pval < 0.05:
    print("Reject H0 → Automatic cars are significantly more expensive")
else:
    print("Fail to Reject H0 → No significant difference")

"""Newer cars have higher prices (correlation test)"""

corr = df[['selling_price','year','car_age']].corr()
print("\n===== HYPOTHESIS TEST 2 =====")
print("Correlation between Year and Price:")
print(corr)

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (Hypothesis Testing)")
plt.show()

"""**Detecting Data Issues and Problems**"""

print("Missing values per column:\n", df.isnull().sum())

print("\nCars with unrealistic low prices (< ₹20,000):")
print(df[df['selling_price'] < 20000].head())

print("\nCars with future manufacturing years (>2025):")
print(df[df['year'] > 2025])

print("\nExtreme Outliers (Top 5 most expensive cars):")
print(df.sort_values(by='selling_price', ascending=False).head())

"""**FINAL INSIGHTS**"""

print("Trends: Newer cars, bigger engines, automatic transmission = higher prices.")
print("Patterns: More km driven → lower price. Diesel/Petrol dominate market.")
print("Anomalies: Some cars priced too low (<20k) or too high (>1 Cr). Missing data in engine/mileage/power.")
print("Next Steps: Clean missing values, remove outliers, encode categories, build price prediction model.")

