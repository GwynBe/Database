import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Z0mbj3123",
database="store_cms_plusplus_2"
)

mycursor = mydb.cursor()

maker = input("Nhập tên hãng muốn tìm: ")
mycursor.execute("SELECT * FROM store_cms_plusplus_2.laptop WHERE maker LIKE" + "'%" + maker + "%';")
result = mycursor.fetchall()
print(result)

laptop_type = input("Nhập loại máy: ")
mycursor.execute("SELECT * FROM store_cms_plusplus_2.laptop WHERE type LIKE" + "'%" + laptop_type + "%';")
result = mycursor.fetchall()
print(result)

resolution = input("Nhập độ phân giải màn hình: ")
mycursor.execute("SELECT * FROM store_cms_plusplus_2.laptop WHERE screen_resolution LIKE" + "'%" + resolution + "%';")
result = mycursor.fetchall()
print(result)

mycursor.execute("SELECT * FROM store_cms_plusplus_2.laptop WHERE price > 10000000 and sold >= 30;")
result = mycursor.fetchall()
print(f"Laptop giá trên 10000000 và sold >= 30: {result}")


mycursor.execute("SELECT * FROM store_cms_plusplus_2.laptop WHERE price BETWEEN 10000000 AND 20000000;")
result = mycursor.fetchall()
print(result)