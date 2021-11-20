import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="123456",
database="store_cms_plusplus"
)

mycursor = mydb.cursor()

def insert_laptop(name, url, maker, type, ram, cpu, ssd, hdd, price, card, screen_resolution, screen_size, sold):
    querry = "INSERT IGNORE INTO store_cms_plusplus.laptop (`name`, url, maker, `type`, ram, `cpu`, ssd, hdd, price, card, screen_resolution, screen_size, sold) VALUES \
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    values = (name, url, maker, type, ram, cpu, ssd, hdd, price, card, screen_resolution, screen_size, sold)
    mycursor.execute(querry, values)
    mydb.commit()

insert_laptop("A1", "google.com", "AAA", "A_laptop", "8GB", "i5", "128GB", "0GB", 10000000, "GTX", "FHD 1080", "14 inch", 1)

mycursor.execute("SELECT * FROM store_cms_plusplus.laptop WHERE name LIKE '%a1%'")

result = mycursor.fetchall()

print(result)
