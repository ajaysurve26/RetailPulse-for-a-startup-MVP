import streamlit as st
import json
import pandas as pd
import time

# Optional: Replace experimental_set_query_params warning
# Set auto-refresh interval (in seconds)
refresh_interval = 5  # Refresh every 5 seconds

# Mapping store and product IDs to friendly names
store_names = {
    "TX303": "Texas Outlet",
    "FL404": "Florida Supercenter",
    "NY001": "New York Central",
    "CA202": "California Hub"
}

product_names = {
    "SKU001": "Wireless Mouse",
    "SKU002": "Mechanical Keyboard",
    "SKU003": "HD Monitor",
    "SKU004": "USB-C Hub"
}

# Load JSON data
with open('live_sales_metrics.json', 'r') as f:
    data = json.load(f)

# Extract and combine store-wise data
store_sales = data.get('store_sales', {})
store_revenue = data.get('store_revenue', {})
top_products = data.get('top_products', [])

store_data = [
    {
        'Store': store_names.get(store, store),
        'Items Sold': store_sales.get(store, 0),
        'Revenue': store_revenue.get(store, 0.0)
    }
    for store in store_sales
]
df = pd.DataFrame(store_data)

# Streamlit layout
st.set_page_config(page_title="Real-Time Retail Dashboard", layout="centered")
st.title("🛒 Real-Time Retail Dashboard")
st.caption(f"Refreshing every {refresh_interval} seconds...")
st.caption(f"Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Store Performance Table
st.subheader("📍 Store Performance Overview")
st.dataframe(df)

# Bar Chart: Revenue by Store
st.subheader("💰 Revenue by Store")
rev_df = df.set_index('Store')['Revenue']
st.bar_chart(rev_df)

# Bar Chart: Items Sold by Store
st.subheader("📦 Items Sold by Store")
items_df = df.set_index('Store')['Items Sold']
st.bar_chart(items_df)

# Top Products Section
st.subheader("🏆 Top Selling Products")
for i, (product, count) in enumerate(top_products, 1):
    product_name = product_names.get(product, product)
    st.write(f"{i}. {product_name} — {count} units")

# Auto-refresh
time.sleep(refresh_interval)
st.rerun()