
import csv
import datetime
import os

def load_products():
    product_dict = {}
    with open('products.csv ', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            product_id = row[0]
            product_name = row[1]
            product_price = row[2]

            product_dict[product_id] = {
                "name": product_name,
                "price": int(product_price)
            }
    return product_dict

def main():
    print('Starting Sales Tracker...')

    try:
        products = load_products()
        print(f"Loaded {len(products)} products")

    except:
        print('Error: Cannot load products.csv')
        return

    try:
        with open('raw_product_sales', 'r') as file:
            sales_ids = file.readlines()
        print(f'Loaded {len(sales_ids)} sales')
    except:
        print('Error: Cannot load sales file')
        return

    processed_sales = []
    sale_id = 1
    current_date = datetime.date.today()

    print("Processing sales...")
    for sale in sales_ids:
        clean_id = sale.strip()


        product_name = products[clean_id]["name"]
        product_price = products[clean_id]["price"]


        sale_record = [current_date, sale_id, clean_id, product_name, product_price]


        processed_sales.append(sale_record)


        sale_id += 1


    print("Creating CSV file...")
    with open('sales_report.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

            # Write headers
        csvwriter.writerow(["Date", "Sale_ID", "Product_ID", "Product_Name", "Unit_Price"])

            # Write all sales data
        csvwriter.writerows(processed_sales)

    print(f"CSV created with {len(processed_sales)} sales!")
    print("Program finished!")

main()