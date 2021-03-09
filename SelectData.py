import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="phuangkaeo",
    password="simplon59",
    database="ecommerce"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(DISTINCT customer_id) AS TOT_CUSTOMER "
                 "FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)