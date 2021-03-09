import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="phuangkaeo",
    password="simplon59",
    database="ecommerce"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE geolocation ("
                 "geolocation_zip_code_prefix INT NOT NULL,"
                 "geolocation_lat DECIMAL(25,15),"
                 "geolocation_lng DECIMAL(25,15),"
                 "geolocation_city VARCHAR(25),"
                 "geolocation_state VARCHAR(10),"
                 "PRIMARY KEY (geolocation_zip_code_prefix))"
                 "ENGINE=INNODB"
                 )

mycursor.execute("CREATE TABLE customers ("
                 "customer_id VARCHAR(50) NOT NULL,"
                 "customer_unique_id VARCHAR(50),"
                 "customer_zip_code_prefix INT,"
                 "customer_city VARCHAR(50),"
                 "customer_state VARCHAR(50),"
                 "PRIMARY KEY (customer_id),"
                 "FOREIGN KEY (customer_zip_code_prefix) REFERENCES geolocation(geolocation_zip_code_prefix))"
                 "ENGINE=INNODB"
                 )

mycursor.execute("CREATE TABLE orders (order_id VARCHAR(50) NOT NULL,"
                 "customer_id VARCHAR(50),"
                 "order_status VARCHAR(50),"
                 "order_purchase_timestamp DATETIME,"
                 "order_approved_at DATETIME,"
                 "order_delivered_carrier_date DATETIME,"
                 "order_delivered_customer_date DATETIME,"
                 "order_estimated_delivery_date DATETIME,"
                 "FOREIGN KEY (customer_id) REFERENCES customers(customer_id),"
                 "PRIMARY KEY (order_id))"
                 "ENGINE=INNODB"
                 )

mycursor.execute("CREATE TABLE orders_payment (payment_id INT NOT NULL AUTO_INCREMENT,"
                 "order_id VARCHAR(50),"
                 "payment_sequential VARCHAR(2),"
                 "payment_type VARCHAR(20),"
                 "payment_installments INT,"
                 "payment_value DECIMAL(4,2),"
                 "FOREIGN KEY (order_id) REFERENCES orders(order_id),"
                 "PRIMARY KEY (payment_id))"
                 "ENGINE=INNODB"
                 )

mycursor.execute("CREATE TABLE orders_reviews (review_id VARCHAR(50) NOT NULL,"
                 "order_id VARCHAR(50),"
                 "review_score INT,"
                 "review_comment_title VARCHAR(255),"
                 "review_comment_message VARCHAR(255),"
                 "review_creation_date DATETIME,"
                 "review_answer_timestamp DATETIME,"
                 "FOREIGN KEY (order_id) REFERENCES orders(order_id),"
                 "PRIMARY KEY (review_id))"
                 "ENGINE=INNODB"
                 )

mycursor.execute("CREATE TABLE sellers (seller_id VARCHAR(50) NOT NULL,"
                 "seller_zip_code_prefix INT,"
                 "seller_city VARCHAR(25),"
                 "seller_state VARCHAR(10),"
                 "FOREIGN KEY (seller_zip_code_prefix) REFERENCES geolocation(geolocation_zip_code_prefix),"
                 "PRIMARY KEY (seller_id))"
                 "ENGINE=INNODB"
                 )

mycursor.execute("CREATE TABLE products (product_id VARCHAR(50) NOT NULL,"
                 "product_category_name VARCHAR(25),"
                 "product_name_lenght INT,"
                 "product_description_lenght INT,"
                 "product_photos_qty INT,"
                 "product_weight_g INT,"
                 "product_length_cm INT,"
                 "product_height_cm INT,"
                 "product_width_cm INT,"
                 "PRIMARY KEY (product_id))"
                 "ENGINE=INNODB"
                 )

mycursor.execute("CREATE TABLE orders_items ("
                 "order_id VARCHAR(50),"
                 "order_item_id VARCHAR(50) NOT NULL,"
                 "product_id VARCHAR(50),"
                 "seller_id VARCHAR(50),"
                 "shipping_limit_date DATETIME,"
                 "price DECIMAL(10,2),"
                 "freight_value DECIMAL(10,2),"
                 "FOREIGN KEY (order_id) REFERENCES orders(order_id),"
                 "FOREIGN KEY (product_id) REFERENCES products(product_id),"
                 "FOREIGN KEY (seller_id) REFERENCES sellers(seller_id),"
                 "PRIMARY KEY (order_item_id))"
                 "ENGINE=INNODB"
                 )
#
