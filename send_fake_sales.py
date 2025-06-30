from kafka import KafkaProducer
from faker import Faker
import json
import time
import random

fake = Faker()

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Sample store and product IDs
store_ids = ['NY001', 'CA202', 'TX303', 'FL404']
product_ids = ['SKU001', 'SKU002', 'SKU003', 'SKU004']

# Send a new sale every 2 seconds
while True:
    sale = {
        'store_id': random.choice(store_ids),
        'product_id': random.choice(product_ids),
        'timestamp': time.time(),
        'amount': round(random.uniform(5.0, 500.0), 2),
        'customer_name': fake.name()
    }

    producer.send('sales_topic', sale)
    print(f"Sent: {sale}")
    time.sleep(2)