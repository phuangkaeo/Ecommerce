import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="phuangkaeo",
    password="simplon59"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE ecommerce")
