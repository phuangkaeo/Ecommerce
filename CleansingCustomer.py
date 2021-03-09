import pandas as pd
import mysql.connector
from sqlalchemy.types import Integer, String, Float, DateTime
from sqlalchemy import create_engine

mydb = mysql.connector.connect(
    host="localhost",
    user="phuangkaeo",
    password="simplon59",
    database="ecommerce")

engine = create_engine('mysql+pymysql://phuangkaeo:simplon59@localhost/ecommerce')

customer = pd.read_csv('data/olist_customers_dataset.csv')
location = pd.read_csv('data/olist_geolocation_dataset.csv')
order_item = pd.read_csv('data/olist_order_items_dataset.csv')
order_payment = pd.read_csv('data/olist_order_payments_dataset.csv')
order_reviews = pd.read_csv('data/olist_order_reviews_dataset.csv')
orders = pd.read_csv('data/olist_orders_dataset.csv')
product = pd.read_csv('data/olist_products_dataset.csv')
sellers = pd.read_csv('data/olist_sellers_dataset.csv')


##CHECK DUPLICATEDATA ON PRODUCTS TABLE
print(order_item.head())
# #check null values
# print(order_payment.isnull().sum())
# #count row
# print(order_payment.count())
# #check duplicate
# print(order_payment.drop_duplicates())
#
#write to mysql
order_item.to_sql(
    name="orders_items",
    con=engine,
    index=False,
    if_exists='replace',
    dtype={'order_id':String(50),
           'order_item_id': String(50),
           'product_id': String(50),
           'seller_id': String(50),
           'shipping_limit_date': DateTime,
           'price':Float,
           'freight_value':Float})