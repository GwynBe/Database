import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="123456",
database="mydb"
)

mycursor = mydb.cursor()

def Login(phone, password):
    querry = "SELECT * FROM mydb.users WHERE %s = PHONE AND %s = PASSWORD"
    values = (phone, password)
    mycursor.execute(querry, values)
    result = mycursor.fetchall()
    if result != []:
        print("Login success")
    else:
        print("Login failed")

def Signin(phone, password, email, user_name):
    querry = "INSERT INTO mydb.users (PHONE, `PASSWORD`, EMAIL, USER_NAME) VALUES (%s, %s, %s, %s)"
    values = (phone, password, email, user_name)
    try:
        mycursor.execute(querry, values)
        mydb.commit()
        print("Success!")
    except:
        print("Đăng ký thất bại, kiểm tra lại sđt")

Signin(123456, 'ghi', 'ghi@gmail.com', 'ghi')

Login(123456, 'abc')

def Insert_book(id, title, year, des, author, price, genre, url, contact):
    querry = "INSERT INTO mydb.books ("