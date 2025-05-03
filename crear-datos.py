import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
products = ["Laptop", "Phone", "Tablet", "Headphones"]
categories = ["Electronics", "Accessories"]
data = {
    "Date": np.random.choice(dates, 50),
    "Product": np.random.choice(products, 50),
    "Category": np.random.choice(categories, 50),
    "Price": np.random.uniform(50, 500, 50).round(2),
    "Quantity": np.random.randint(1, 5, 50)
}
df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]
df.to_csv("sales_data.csv", index=False)
print("Archivo sales_data.csv generado exitosamente.")