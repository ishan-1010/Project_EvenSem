import csv
import random
import datetime
import uuid

# Generate random data for the CSV


def generate_csv_data():
    # Load product names from products.csv with UTF-8 encoding
    with open(r"C:\Users\Ishan\Downloads\instacart-market-basket-analysis\products.csv", 'r', encoding='utf-8') as products_file:
        products_reader = csv.DictReader(products_file)
        product_names = [row['product_name'] for row in products_reader]

    # Load order IDs from orders.csv
    with open(r"C:\Users\Ishan\Downloads\instacart-market-basket-analysis\orders.csv", 'r') as orders_file:
        orders_reader = csv.DictReader(orders_file)
        order_ids = [row['order_id'] for row in orders_reader]

    # Generate CSV data
    csv_data = []
    for username in range(1, 101):
        for _ in range(random.randint(3, 21)):
            transaction_id = str(uuid.uuid4())[:8]
            invoice_number = f'INV{random.randint(1000, 9999)}'
            date = datetime.date(random.randint(
                2015, 2023), random.randint(1, 12), random.randint(1, 28))
            order_id = random.choice(order_ids)
            amount_paid = round(random.uniform(1.0, 1000.0), 2)
            product_name = random.choice(product_names)
            csv_data.append((username, transaction_id, invoice_number, date,
                            order_id, amount_paid, product_name))

    return csv_data

# Write CSV data to file


def write_csv_file(file_name):
    csv_data = generate_csv_data()

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['UserName', 'Transaction ID', 'Invoice Number', 'Date of Transaction',
                         'Order ID', 'Amount Paid', 'Product Name'])
        writer.writerows(csv_data)

    print(f'{file_name} generated successfully.')


# Generate the CSV file
write_csv_file('generated_data.csv')
