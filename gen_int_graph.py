import seaborn as sns
import plotly.graph_objects as go
import sys
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import numpy as np


# Load the Instacart Market Basket Analysis dataset
orders = pd.read_csv(
    r"C:\Users\Ishan\Downloads\instacart-market-basket-analysis\orders.csv")
order_products = pd.read_csv(
    r"C:\Users\Ishan\Downloads\instacart-market-basket-analysis\order_products__prior.csv")
departments = pd.read_csv(
    r"C:\Users\Ishan\Downloads\instacart-market-basket-analysis\departments.csv")
aisles = pd.read_csv(
    r"C:\Users\Ishan\Downloads\instacart-market-basket-analysis\aisles.csv")
products = pd.read_csv(
    r"C:\Users\Ishan\Downloads\instacart-market-basket-analysis\products.csv")

# Merge relevant datasets
orders_products = pd.merge(order_products, products,
                           on='product_id', how='left')
orders_products = pd.merge(orders_products, aisles, on='aisle_id', how='left')
orders_products = pd.merge(
    orders_products, departments, on='department_id', how='left')

# Department-wise Sales - Stacked Bar Chart
department_wise_sales = order_products.merge(products, on='product_id', how='left').merge(
    departments, on='department_id', how='left')
department_wise_sales = department_wise_sales.groupby(
    ['department', 'reordered'])['product_id'].count().unstack().fillna(0)
department_wise_sales['Total'] = department_wise_sales.sum(axis=1)
department_wise_sales['Reorder Rate'] = department_wise_sales[1] / \
    department_wise_sales['Total']
department_wise_sales = department_wise_sales.sort_values(
    by='Reorder Rate', ascending=False)
# Increase figure size and rotate x-axis labels
plt.figure(figsize=(16, 8))
plt.bar(department_wise_sales.index,
        department_wise_sales[1], label='Reordered')
plt.bar(department_wise_sales.index,
        department_wise_sales[0], bottom=department_wise_sales[1], label='Not Reordered')
plt.xlabel('Department')
plt.ylabel('Product Count')
plt.title('Department-wise Sales with Reorder Rate')
plt.legend()
# adjust rotation and font size
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.subplots_adjust(bottom=0.25)  # adjust bottom margin
plt.savefig('dept_graph.png')
plt.show()
# Aisle-wise Sales - Stacked Bar Chart
aisle_wise_sales = order_products.merge(
    products, on='product_id', how='left').merge(aisles, on='aisle_id', how='left')
aisle_wise_sales = aisle_wise_sales.groupby(['aisle', 'reordered'])[
    'product_id'].count().unstack().fillna(0)
aisle_wise_sales['Total'] = aisle_wise_sales.sum(axis=1)
aisle_wise_sales['Reorder Rate'] = aisle_wise_sales[1] / \
    aisle_wise_sales['Total']
aisle_wise_sales = aisle_wise_sales.sort_values(
    by='Reorder Rate', ascending=False)
plt.figure(figsize=(16, 12))
plt.bar(aisle_wise_sales.index, aisle_wise_sales[1], label='Reordered')
plt.bar(aisle_wise_sales.index, aisle_wise_sales[0],
        bottom=aisle_wise_sales[1], label='Not Reordered')
plt.xlabel('Aisle')
plt.ylabel('Product Count')
plt.title('Aisle-wise Sales with Reorder Rate')
plt.legend()
# only display every 5th aisle label
xtick_locations = np.arange(0, len(aisle_wise_sales), 5)
xtick_labels = aisle_wise_sales.index[xtick_locations]
plt.xticks(xtick_locations, xtick_labels, rotation=40, ha='right', fontsize=6)
plt.savefig('aisle_graph.png')
plt.show()
customer_order_frequency = orders['user_id'].value_counts(
).value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.bar(customer_order_frequency.index, customer_order_frequency.values)
plt.xlabel('Number of Orders per Customer')
plt.ylabel('Number of Customers')
plt.title('Customer Order Frequency')
plt.xticks(np.arange(1, max(customer_order_frequency.index) + 1, 5),
           np.arange(1, max(customer_order_frequency.index) + 1, 5))
plt.savefig('cust_ord_graph.png')
plt.show()
order_frequency_by_dow = orders.groupby(['user_id', 'order_dow'])[
    'order_number'].count().unstack().count().sort_index()
plt.figure(figsize=(10, 6))
plt.bar(order_frequency_by_dow.index, order_frequency_by_dow.values)
plt.xlabel('Order Day of Week')
plt.ylabel('Number of Customers')
plt.title('Order Frequency by Day of Week')
plt.xticks(range(7), ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
plt.savefig('freq_graph.png')
plt.show()


product_popularity = orders_products['product_name'].value_counts().nlargest(
    15)
plt.figure(figsize=(16, 6))
plt.barh(product_popularity.index, product_popularity.values)
plt.xlabel('Number of Orders')
plt.ylabel('Product Name')
plt.title('Top 15 Product Popularity')

plt.savefig('top15_graph.png')
plt.show()


order_frequency_by_dow_hour = orders.groupby(['order_dow', 'order_hour_of_day'])[
    'order_id'].count().unstack().fillna(0)
plt.figure(figsize=(10, 6))
sns.heatmap(order_frequency_by_dow_hour, cmap='YlGnBu',
            fmt='d', cbar_kws={'label': 'Number of Orders'})
plt.xlabel('Order Hour of Day')
plt.ylabel('Order Day of Week')
plt.title('Order Frequency Heatmap')
plt.xticks(range(24))
plt.yticks(range(7), ['Sun', 'Mon', 'Tue', 'Wed',
           'Thu', 'Fri', 'Sat'], rotation=360)

plt.savefig('freq_dow_graph.png')
plt.show()
