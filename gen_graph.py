import sys
import pandas as pd
import matplotlib.pyplot as plt

# Read data from the Instacart Kaggle dataset
orders_df = pd.read_csv(
    r"C:\Users\Ishan\Downloads\instacart-market-basket-analysis\orders.csv")
order_products_prior_df = pd.read_csv(
    r"C:\Users\Ishan\Downloads\instacart-market-basket-analysis\order_products__prior.csv")
products_df = pd.read_csv(
    r"C:\Users\Ishan\Downloads\instacart-market-basket-analysis\products.csv")

# Get specific user's order data


def get_user_order_data(username):
    user_orders = orders_df[orders_df['user_id'] == username]
    user_order_ids = user_orders['order_id'].unique()
    user_order_products = order_products_prior_df[order_products_prior_df['order_id'].isin(
        user_order_ids)]
    user_order_data = pd.merge(user_orders, user_order_products, on='order_id')
    return user_order_data

# Generate and save different graphs for the specific user


def generate_user_graphs(username):
    user_order_data = get_user_order_data(username)

    # Generate graph 1: Order count by day of week
    order_count_by_dow = user_order_data['order_dow'].value_counts(
    ).sort_index()
    plt.figure()
    order_count_by_dow.plot(kind='bar', rot=0)
    plt.title('Order Count by Day of Week for User ' + str(username))
    plt.xlabel('Day of Week')
    plt.ylabel('Order Count')
    plt.savefig('user_' + str(username) + '_order_count_by_dow.png')

    # Generate graph 2: Hourly order count distribution
    order_count_by_hour = user_order_data['order_hour_of_day'].value_counts(
    ).sort_index()
    plt.figure()
    order_count_by_hour.plot(kind='bar', rot=0)
    plt.title('Hourly Order Count Distribution for User ' + str(username))
    plt.xlabel('Hour of Day')
    plt.ylabel('Order Count')
    plt.savefig('user_' + str(username) + '_order_count_by_hour.png')

    # Generate graph 3: Most ordered products
    top_n = 10
    user_order_products_count = user_order_data['product_id'].value_counts().head(
        top_n)
    top_products = pd.merge(user_order_products_count,
                            products_df, on='product_id')
    # Drop duplicates based on 'product_name'
    top_products = top_products.drop_duplicates(subset='product_name')

    plt.figure()
    top_products.plot(x='product_name', y='product_id', kind='barh')
    plt.title('Most Ordered Products for User ' + str(username))
    plt.xlabel('Order Count')
    plt.ylabel('Product Name')
    plt.tick_params(axis='y', labelsize=6)
    plt.tight_layout()  # Adjust layout to prevent labels from getting cut off
    plt.savefig('user_' + str(username) + '_most_ordered_products.png')


# Example usage: Get username from command-line argument

if len(sys.argv) != 2:
    print('Usage: generate_graphs.py <username>')
else:
    username = int(sys.argv[1])
    generate_user_graphs(username)
