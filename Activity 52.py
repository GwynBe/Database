import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="123456",
database="store_cms_plusplus"
)

mycursor = mydb.cursor()

id = input("Nhập id: ")

sold = input("Nhập số lượng: ")
 

mycursor.execute(f"UPDATE store_cms_plusplus.laptop SET sold = {sold}, last_updated_timestamp = now() WHERE id = {id}")

mycursor.fetchall()

mycursor.execute(f"SELECT id, sold from store_cms_plusplus.laptop WHERE id = {id}")

print(mycursor.fetchall())