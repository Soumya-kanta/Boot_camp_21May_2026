import pandas as pd
import os
import json
import logging
from datetime import datetime

os.makedirs(r'C:\Users\ASUS\Downloads\StratLytics_Coding_Test_Learner_Files\logs', exist_ok = True)
os.makedirs(r'C:\Users\ASUS\Downloads\StratLytics_Coding_Test_Learner_Files\output', exist_ok = True)

logging.basicConfig(
    filename = r'C:\Users\ASUS\Downloads\StratLytics_Coding_Test_Learner_Files\logs\my_log.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)
logging.info('Logging file created successfully')

customer = pd.read_csv(r'C:\Users\ASUS\Downloads\StratLytics_Coding_Test_Learner_Files\input_data\customers.csv')
orders = pd.read_csv(r'C:\Users\ASUS\Downloads\StratLytics_Coding_Test_Learner_Files\input_data\orders.csv')
logging.info('All files are read successfully')

global product_clean
product_clean = []
malformed = 0
with open(r'C:\Users\ASUS\Downloads\StratLytics_Coding_Test_Learner_Files\input_data\products.json') as f:
    data = json.load(f)
    for item in data:
        try:
            product_clean.append({
                'product_id': item['product_id'],
                'product_name': item['product_name'],
                'category': item['category'],
                'price': item['price']
            })
        except:
            malformed += 1
logging.info(f'Products file read successfully with {malformed} malformed records')


def customer_data(customer):
    global customer_clean, customer_reject, invalid_values
    invalid_values = ["", "null", "na"]
    customer = customer.replace(invalid_values, pd.NA)
    customer['signup_date'] = pd.to_datetime(customer['signup_date'], errors='coerce')
    customer_clean = customer.dropna(subset=["customer_id", "name", "email", "signup_date", "country"]).copy()
    customer_reject = customer[customer[["customer_id", "name", "email", "signup_date", "country"]].isna().any(axis=1)].copy()
    customer_reject["error"] = "Invalid customer data"
    customer_clean.to_csv(r'C:\Users\ASUS\Downloads\StratLytics_Coding_Test_Learner_Files\output\clean_customers.csv', index=False)
    customer_reject.to_csv(r'C:\Users\ASUS\Downloads\StratLytics_Coding_Test_Learner_Files\output\rejected_customers.csv', index=False)
    logging.info(f'Customer data processed with {len(customer_clean)} clean records and {len(customer_reject)} rejected records')

customer_data(customer)

def order_data(orders):
    orders = orders.replace(invalid_values, pd.NA)
    orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')
    order_clean = orders[
        (orders["quantity"] > 0) &
        (orders["unit_price"] > 0) &
        (orders["status"] == 'continued')
    ].copy()
    order_reject = orders[
        (~orders["quantity"] > 0) |
        (~orders["unit_price"] > 0) |
        (~orders["status"] == 'continued')
    ].copy()
    order_reject["error"] = "Invalid order data"
    order_clean.to_csv(r'C:\Users\ASUS\Downloads\StratLytics_Coding_Test_Learner_Files\output\clean_orders.csv', index=False)
    order_reject.to_csv(r'C:\Users\ASUS\Downloads\StratLytics_Coding_Test_Learner_Files\output\rejected_orders.csv', index=False)

order_data(orders)