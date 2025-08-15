import csv
import datetime
import os

product_data = {
    "P001": {"name": "Wireless Headphones", "price": 100},
    "P002": {"name": "Laptop Backpack", "price": 60},
    "P003": {"name": "Bluetooth Speaker", "price": 50},
    "P004": {"name": "USB Flash Drive", "price": 20},
    "P005": {"name": "Mobile Phone Case", "price": 15},
    "P006": {"name": "Wireless Mouse", "price": 30},
    "P007": {"name": "Laptop Stand", "price": 40},
    "P008": {"name": "HDMI Cable", "price": 15},
    "P009": {"name": "Smartphone", "price": 600},
    "P010": {"name": "External Hard Drive", "price": 100}
}

# Read the raw product sales file
with open('raw_product_sales', 'r') as file:
    product_ids = file.readlines()

sales_data = []
current_date = datetime.date.today()
sale_id = 1

# Process each product ID
for product_id in product_ids:
    clean_id = product_id.strip()

    # Skip empty lines
    if not clean_id:
        continue

    # Get product data
    product_name = product_data[clean_id]['name']
    product_price = product_data[clean_id]['price']
    sale_record = [current_date, sale_id, clean_id, product_name, product_price]
    sales_data.append(sale_record)
    sale_id += 1

# Create CSV file
with open('product_sales.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Date", "Sale_ID", "Product_ID", "Product_Name", "Unit_Price"])
    csv_writer.writerows(sales_data)

print("CSV file created successfully!")
print(f"Total sales processed: {len(sales_data)}")