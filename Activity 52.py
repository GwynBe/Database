import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="123456",
database="store_cms_plusplus"
)

mycursor = mydb.cursor()

def update_laptop(id, sold):
 
    querry = "UPDATE store_cms_plusplus.laptop SET sold = %s, last_updated_timestamp = now() WHERE id = %s"
    values = (sold, id)
    mycursor.execute(querry, values)
    mydb.commit()

update_laptop(1, 1000)
