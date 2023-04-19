import csv
import random
from datetime import datetime, timedelta

# Define user IDs
user_ids = [1, 2, 3]

# Define the number of entries per user
num_entries = 1000

# Generate data for each user
for user_id in user_ids:
    # Create a unique CSV file for each user
    file_name = f"user_{user_id}_data.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ["UserID", "InvoiceNo", "DateOfTransaction", "OrderID", "ProductID"])
        for i in range(num_entries):
            invoice_no = random.randint(1000, 9999)
            date_of_transaction = (
                datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')
            order_id = random.randint(10000, 99999)
            product_id = random.randint(1, 100)
            writer.writerow(
                [user_id, invoice_no, date_of_transaction, order_id, product_id])
    print(f"{file_name} created with {num_entries} entries.")
