from kafka import KafkaConsumer
import json
from collections import defaultdict, Counter

# Create Kafka consumer
consumer = KafkaConsumer(
    'sales_topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='retail-analytics'
)

print("🟢 Listening to 'sales_topic'...")

# Set up data structures
store_sales = defaultdict(int)
store_revenue = defaultdict(float)
product_counter = Counter()

# Loop to process messages
for message in consumer:
    sale = message.value
    store = sale['store_id']
    product = sale['product_id']
    amount = sale['amount']
    quantity = sale.get('quantity_sold', 1)

    # Update totals
    store_sales[store] += quantity
    store_revenue[store] += amount
    product_counter[product] += quantity

    # Print live metrics
    print("\n📊 Live Store Analytics:")
    for s in store_sales:
        print(f"  - {s}: {store_sales[s]} items sold | ${store_revenue[s]:.2f} revenue")

    top_products = product_counter.most_common(3)
    print("\n🏆 Top 3 Products:")
    for i, (product, count) in enumerate(top_products, 1):
        print(f"  {i}. {product}: {count} units sold")

    # ✅ Save to JSON so Streamlit can read it
    serializable_metrics = {
        "store_sales": dict(store_sales),
        "store_revenue": dict(store_revenue),
        "top_products": top_products
    }

    with open("live_sales_metrics.json", "w") as f:
        json.dump(serializable_metrics, f)