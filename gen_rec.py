import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import random

# Load the Instacart dataset - read only first 1000 rows
# Replace with the actual path to the products.csv file
products_df = pd.read_csv(
    r"C:\Users\Ishan\Downloads\instacart-market-basket-analysis\products.csv")
# Replace with the actual path to the order_products__prior.csv file
orders_df = pd.read_csv(
    r"C:\Users\Ishan\Downloads\instacart-market-basket-analysis\order_products__prior.csv", nrows=500000)

# Specify the user ID to generate recommendations for
user = 1

# Get the products ordered by the selected user
user_products = orders_df.loc[orders_df['order_id']
                              == user, 'product_id'].tolist()

# Calculate similarity scores using Jaccard similarity


def jaccard_similarity(a, b):
    intersection_cardinality = len(set(a) & set(b))
    union_cardinality = len(set(a) | set(b))
    return intersection_cardinality / float(union_cardinality)


# Calculate similarity scores for all orders
similarity_scores = {}
for order in orders_df['order_id'].unique():
    if order != user:
        order_products = orders_df.loc[orders_df['order_id']
                                       == order, 'product_id'].tolist()
        similarity_scores[order] = jaccard_similarity(
            user_products, order_products)

# Sort users by similarity score in descending order
similarity_scores = sorted(
    similarity_scores.items(), key=lambda x: x[1], reverse=True)

# Get product recommendations from top similar users
num_recommendations = 5  # Number of recommendations to generate
recommended_user_orders = [user[0]
                           for user in similarity_scores[:num_recommendations]]
recommended_product_ids = orders_df.loc[orders_df['order_id'].isin(
    recommended_user_orders), 'product_id'].value_counts().index.tolist()

# Get product names from product IDs
recommended_product_names = products_df.loc[products_df['product_id'].isin(
    recommended_product_ids), 'product_name']

# If less than 5 recommendations are found, randomly sample from all product names
if len(recommended_product_names) < 5:
    all_product_names = products_df['product_name']
    recommended_product_names = recommended_product_names.append(
        all_product_names.sample(5 - len(recommended_product_names)))

# Limit the number of recommendations to 5
recommended_product_names = recommended_product_names[:5]

# Store recommendations in a file for the current user
username = f"user{user}"
with open(f"{username}_recommendations.txt", "w") as file:
    file.write(f"Recommended products for {username}:\n")
    for product in recommended_product_names:
        file.write(product + "\n")
