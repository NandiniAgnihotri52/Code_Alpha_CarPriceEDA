**Car Price Exploratory Data Analysis (EDA)**



**Project Overview**

This project performs Exploratory Data Analysis (EDA) on a dataset of used cars.

The goal is to identify trends, patterns, anomalies, and test hypotheses to understand factors affecting car prices.



Dataset: `Car\\\_details\\\_v3.csv`



**Steps Covered**

1\.  **Ask meaningful questions**

   - How does car price vary with year, mileage, and power?

   - Do automatic cars cost more than manual cars?

   - Does fuel type significantly affect price?



2\.  **Explore the data structure**

   - Data types, missing values, summary statistics.



3\.  **Identify trends, patterns, anomalies**

   - Price vs year (newer cars are costlier).

   - Automatic cars are generally priced higher.

   - Outliers found in extremely low/high prices.



4\.  **Test hypotheses \& validate assumptions**

   - Automatic vs Manual prices → \*t-test\*.

   - Car Year vs Price → \*correlation analysis\*.



5\.  **Detect issues / problems**

   - Missing values in mileage, engine, max\_power.

   - Unrealistic selling prices (< ₹20,000 or > ₹1 Cr).

   - Cars with future years (>2025).



---



&nbsp;**Tools \& Libraries**

\- Python

\- Pandas, NumPy

\- Matplotlib, Seaborn

\- SciPy (for hypothesis testing)



---



 **How to Run**

1\. Clone the repo:

   ```bash

   git clone https://github.com/yourusername/car-price-eda.git

