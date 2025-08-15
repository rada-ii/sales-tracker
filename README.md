# Sales Tracker

Automates sales data processing by converting product ID lists into detailed CSV reports with product names, prices, and transaction data.

## What It Does

Reads a text file containing product IDs and generates a comprehensive sales report with:
- Sequential transaction IDs
- Current date timestamp
- Product names and prices
- Formatted CSV output

## Input/Output Example

**Input** (`raw_product_sales.txt`):
```
P005
P001
P006
P003
```

**Output** (`sales_report.csv`):
```csv
Date,Sale_ID,Product_ID,Product_Name,Unit_Price
2025-08-15,1,P005,Mobile Phone Case,15
2025-08-15,2,P001,Wireless Headphones,100
2025-08-15,3,P006,Wireless Mouse,30
2025-08-15,4,P003,Bluetooth Speaker,50
```

## How to Run

```bash
# Basic version (embedded product data)
python sales_tracker.py

# Advanced version (CSV product catalog)
python sales_tracker_advanced.py
```

## Files

- `sales_tracker.py` - Basic version with hardcoded product database
- `sales_tracker_advanced.py` - Advanced version with external CSV catalog
- `products.csv` - Product database (ID, name, price)
- `raw_product_sales.txt` - Input transaction data

## Versions

**Basic:** Uses embedded product data, single file solution, fast processing.

**Advanced:** Reads products from CSV, includes error handling, easily updatable catalog.

## Benefits

Converts manual data entry (hours) into automated processing (seconds). Eliminates human errors and ensures consistent formatting.
