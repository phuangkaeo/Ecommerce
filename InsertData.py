import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="phuangkaeo",
    password="simplon59",
    database="ecommerce"
)

cur = mydb.cursor()

file = open('data/olist_geolocation_dataset.csv')
csv_data = csv.reader(file)

skipHeader = True
for row in csv_data:
    if skipHeader:
        skipHeader = False
        continue
    cur.execute('INSERT INTO geolocation(geolocation_zip_code_prefix, '
                'geolocation_lat,'
                'geolocation_lng,'
                'geolocation_city,'
                'geolocation_state) VALUES(%s,%s,%s,%s,%s)',row)
mydb.commit()
mydb.close()