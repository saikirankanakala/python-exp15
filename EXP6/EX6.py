import pandas as pd

df = pd.read_csv("canteen.csv")
print("CSV file loaded successfully.\n")

df['Sales'] = df['Sales'].fillna(0)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)

month = 1
filtered_data = df[df['Date'].dt.month == month]

print("\nFiltered Data for Month", month)
print(filtered_data)

category_sales = df.groupby('Category')['Sales'].sum()

print("\nTotal Sales by Product Category:")
print(category_sales)