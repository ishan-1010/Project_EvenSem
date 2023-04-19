import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('generated_data.csv', encoding='latin-1')

# Create plot
fig = px.histogram(df, x='Amount Paid', nbins=50,
                   title='Distribution of Amount Paid')
fig.write_image("graph1.png")
fig.show()


# Group data by date and count transactions
df['Date of Transaction'] = pd.to_datetime(df['Date of Transaction'])
df['Date'] = df['Date of Transaction'].dt.date
date_counts = df.groupby('Date')['Transaction ID'].count().reset_index()
date_counts.columns = ['Date', 'Transaction Count']

# Create plot
fig = px.line(date_counts, x='Date', y='Transaction Count',
              title='Transaction Count by Date')
fig.write_image("graph2.png")
fig.show()


# Group data by product name and count transactions
product_counts = df.groupby('Product Name')[
    'Transaction ID'].count().reset_index()
product_counts.columns = ['Product Name', 'Transaction Count']

# Create plot
fig = px.bar(product_counts, x='Product Name', y='Transaction Count',
             title='Transaction Count by Product Name')
fig.write_image("graph4.png")
fig.show()


# Group data by product name and sum amount paid
product_amounts = df.groupby('Product Name')[
    'Amount Paid'].sum().reset_index()
product_amounts.columns = ['Product Name', 'Total Amount Paid']

# Create plot
fig = px.bar(product_amounts, x='Product Name',
             y='Total Amount Paid', title='Total Amount Paid by Product Name')
fig.write_image("graph5.png")
fig.show()


# Group data by product name and calculate average amount paid
product_avg_amounts = df.groupby('Product Name')[
    'Amount Paid'].mean().reset_index()
product_avg_amounts.columns = ['Product Name', 'Average Amount Paid']

# Create plot
fig = px.bar(product_avg_amounts, x='Product Name',
             y='Average Amount Paid', title='Average Amount Paid by Product Name')
fig.write_image("graph6.png")
fig.show()


# Group data by user name and count transactions
user_counts = df.groupby('UserName')['Transaction ID'].count().reset_index()
user_counts.columns = ['User Name', 'Transaction Count']

# Create plot
fig = px.bar(user_counts, x='User Name', y='Transaction Count',
             title='Transaction Count by User Name')
fig.write_image("graph7.png")
fig.show()


# Group data by user name and sum amount paid
user_amounts = df.groupby('UserName')['Amount Paid'].sum().reset_index()
user_amounts.columns = ['User Name', 'Total Amount Paid']

# Create plot
fig = px.bar(user_amounts, x='User Name', y='Total Amount Paid',
             title='Total Amount Paid by User Name')
fig.write_image("graph8.png")
fig.show()
