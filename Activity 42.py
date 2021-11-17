import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="123456",
database="store_cms_plusplus"
)

mycursor = mydb.cursor()

def getCounterbyMaker():
    mycursor.execute(f"SELECT maker, COUNT(maker) as 'quantity' FROM store_cms_plusplus.laptop GROUP BY maker ORDER BY quantity DESC;")
    result = mycursor.fetchall()
    return result

for i in getCounterbyMaker():
    print(f"Maker: {i[0]}, Quantity: {i[1]}")
