import pandas as pd
import numpy as np
from numpy import nan

# Question 1

# 1: Total Amount Spent

df = pd.read_csv('res_purchase_2014.csv')

# Clean the data
df['Amount'] = df['Amount'].str.extract('(\d*\.\d+|\d+)', expand=False)
df['Amount'] = df['Amount'].astype(float)

print(f'Total Amount of Spending: {df["Amount"].sum().round(2)}')


def vendor_total(vendor):
    print(
        f'Total Amount Spent at {vendor}: {df.loc[df["Vendor"] == vendor]["Amount"].sum()}')


# 2: Amount Spent at WW GRAINGER
vendor_total('WW GRAINGER')

# 3: Amount Spent at WM SUPERCENTER
vendor_total('WM SUPERCENTER')

# 4: Amount spent at GROCERY STORES
print(
    f'Total Amount Spent at GROCERY STORES: {df.loc[df["Merchant Category Code (MCC)"] == "GROCERY STORES,AND SUPERMARKETS"]["Amount"].sum()}')


# Question 2

# 1: Read Files
df_bal_sheet = pd.read_excel('Energy.xlsx')
df_ratings = pd.read_excel('EnergyRating.xlsx')

# 2: Drop Columns

# Clean up and replace missing/blank with 0
df_bal_sheet.fillna(0)
df_ratings.fillna(0)
df_bal_sheet.replace({0: np.nan})
df_ratings.replace({0: np.nan})

# Drop cols
df_bal_sheet = df_bal_sheet.dropna(axis=1, thresh=(df_bal_sheet.shape[1])*0.9)
df_ratings = df_ratings.dropna(axis=1, thresh=(df_ratings.shape[1])*0.9)

# 3: Replace all None/Nan with avg. val.
df_bal_sheet = df_bal_sheet.fillna(df_bal_sheet.mean())
df_ratings = df_ratings.fillna(df_ratings.mean())

# 4: Normalize

# Selects number types
bal_num_cols = df_bal_sheet.select_dtypes([np.number])
rating_num_cols = df_ratings.select_dtypes([np.number])


def x_new(x): return (x - x.min())/(x.max() - x.min())


bal_num_cols = bal_num_cols.apply(x_new)
rating_num_cols = rating_num_cols.apply(x_new)
print(bal_num_cols)
print(rating_num_cols)

# 5: Calculate correlation matrix
df_corr = pd.read_excel('Energy.xlsx')

corr_val = df_corr[[
    'Current Assets - Other - Total',
    'Current Assets - Total',
    'Other Long-term Assets',
    'Assets Netting & Other Adjustments']]

print(corr_val.corr())

# 6: New Column Name
df_bal_sheet['Name'] = df_bal_sheet['Company Name'].str.split().str[-1]
print(df_bal_sheet['Company Name'])
print(df_bal_sheet['Name'])

# 7: Merge df_ratings & df_bal_sheet
matched = pd.merge(df_ratings,
                   df_bal_sheet,
                   on=['Data Date', 'Global Company Key'],
                   how='inner')
print(matched)

# 8: Mapping
rate_to_num = {
    'AAA': 0,
    'AA+': 1,
    'AA': 2,
    'AA-': 3,
    'A+': 4,
    'A': 5,
    'A-': 6,
    'BBB+': 7,
    'BBB': 8,
    'BBB-': 9,
    'BB+': 10,
    'BB': 11,
    'others': 12,
    '': 12
}


matched['Rate'] = matched['S&P Domestic Long Term Issuer Credit Rating'].map(
    rate_to_num)

print(matched['S&P Domestic Long Term Issuer Credit Rating'])
print(matched['Rate'])

# 9: Calc Rating Freq

CO = matched.loc[matched['Name'] == 'CO']
ratingfreq = CO['Rate'].mean()
print("Rating Frequency: " + str(ratingfreq))

# 10
matched.to_csv('HW4.csv')
