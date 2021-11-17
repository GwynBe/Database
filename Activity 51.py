import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="123456",
database="store_cms_plusplus"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO store_cms_plusplus.laptop (`name`, url, maker, `type`, ram, `cpu`, ssd, hdd, price, card, screen_resolution, screen_size, sold) VALUES ('A1', 'google.com', 'ASUS', 'A', '8GB', 'i5', '128GB', '0GB', 20000000, 'GTX 5GB', 'FHD 1080', 24, 1);")

mycursor.fetchall()

mycursor.execute("SELECT * FROM store_cms_plusplus.laptop WHERE name LIKE '%a1%'")

result = mycursor.fetchall()

print(result)
