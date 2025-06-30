# RetailPulse-for-a-startup-MVP

A production-ready MVP that simulates live retail sales and delivers store insights via a real-time, auto-refreshing dashboard built with Kafka and Streamlit.

---

## 🚀 Key Features

- **Real-Time Data Streaming** via Apache Kafka (Python-based producer/consumer)
- **Live Analytics Pipeline**: Aggregates items sold, revenue, and top products per store
- **Auto-Updating Dashboard**: Built with Streamlit and Pandas
- **Interactive Visuals**: Store-wise bar charts for sales and revenue
- **ID Mapping**: Product and store names are cleanly mapped from coded IDs
- **Last Updated Timestamp**: Shows real-time update status

---

## 📦 Tech Stack

| Layer              | Tools Used                                  |
|-------------------|----------------------------------------------|
| **Data Streaming** | Apache Kafka + Python `kafka-python`         |
| **ETL Simulation** | Faker + Python Producer Script               |
| **Processing**     | Kafka Consumer + Python Aggregator           |
| **Storage**        | JSON file (`live_sales_metrics.json`)       |
| **Dashboard**      | Streamlit + Pandas + built-in charts        |
| **Deployment**     | Streamlit Cloud or Render (optional)        |

---

