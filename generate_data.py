import pandas as pd

data = {
    'age': [25, 45, 30, 35, 50, 23, 40, 33, 55, 29],
    'income': [50000, 120000, 75000, 100000, 200000, 30000, 95000, 70000, 150000, 85000],
    'loan_amount': [2000, 10000, 5000, 20000, 15000, 3000, 12000, 7000, 20000, 4000],
    'open_accounts': [3, 5, 4, 6, 10, 2, 4, 3, 7, 5],
    'credit_history_length': [2, 20, 8, 15, 25, 1, 18, 10, 30, 7],
    'defaulted_before': [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    'credit_score': [700, 750, 650, 800, 820, 600, 780, 640, 790, 710]
}

df = pd.DataFrame(data)
df.to_csv('credit_data.csv', index=False)
print("Data saved to credit_data.csv")
