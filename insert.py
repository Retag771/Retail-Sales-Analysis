

import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=Retail_sales;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()

base_path = r"C:\Users\aa\Downloads\Ecommerce_Project"

# 1. Customer
cursor.execute(f"""
BULK INSERT customer
FROM '{base_path}\\customer_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
)
""")

# 2. Employee
cursor.execute(f"""
BULK INSERT Employee
FROM '{base_path}\\employee_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
)
""")

# 3. Brand
cursor.execute(f"""
BULK INSERT brand
FROM '{base_path}\\brand_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
)
""")

# 4. Supplier
cursor.execute(f"""
BULK INSERT supplier
FROM '{base_path}\\supplier_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
)
""")

# 5. Promotion
cursor.execute(f"""
BULK INSERT promotion
FROM '{base_path}\\promotion_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
)
""")

# 6. Product
cursor.execute(f"""
BULK INSERT product
FROM '{base_path}\\products_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
)
""")

# 7. Orders
cursor.execute(f"""
BULK INSERT orders
FROM '{base_path}\\orders_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
)
""")

# 8. Order Items
cursor.execute(f"""
BULK INSERT order_items
FROM '{base_path}\\order_items_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
)
""")

# 9. Returns
cursor.execute(f"""
BULK INSERT returns
FROM '{base_path}\\returns_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
)
""")

conn.commit()

print("All data inserted successfully!")

cursor.close()
conn.close()