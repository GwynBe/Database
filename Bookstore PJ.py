import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="123456",
database="book_pj"
)

mycursor = mydb.cursor()

def login(phone, password):
    query = "SELECT * FROM book_pj.users WHERE %s = phone AND %s = password;" %(phone, password)
    mycursor.execute(query)
    result = mycursor.fetchall()
    if result != []:
        print("Đăng nhập thành công")
    else:
        print("Đăng nhập thất bại, kiểm tra lại sđt và mật khẩu")

#login(888, 123)

def signup(name, phone, password, email, info):
    check_query = "SELECT COUNT(%s) FROM book_pj.users;" %(phone)
    mycursor.execute(check_query)
    check_result = mycursor.fetchall()
    if check_result[0][0] > 0:
        print("Số điện thoại đã đăng ký!")
    else:
        query = "INSERT INTO book_pj.users (name, phone, password, email, contact_info) VALUES (%s, %s, %s, %s, %s);" %(name, phone, password, email, info)
        mycursor.execute(query)
        mydb.commit()
        print("Đăng ký thành công")

#signup("abc", 888, "123", "", "abc123")

def insert_genre(main_genre, sub_genre):
    query = "INSERT INTO book_pj.genre (main_genre, sub_genre) VALUES ('%s', '%s');" %(main_genre, sub_genre)
    mycursor.execute(query)
    mydb.commit()

#insert_genre("A", "A1")

def insert_author(name, birth_day, birth_place, background):
    query = "INSERT INTO book_pj.author (name, birth_day, birth_place, background) \
        VALUES ('%s', '%s', '%s', '%s');" %(name, birth_day, birth_place, background)
    mycursor.execute(query)
    mydb.commit()

#insert_author("Tuan Anh", "1993-11-23", "BG", "")    

def insert_picture(main_picture_url, side_picture_url):
    query = "INSERT INTO book_pj.picture_url (main_picture_url, side_picture_url) VALUES ('%s', '%s');" %(main_picture_url, side_picture_url)
    mycursor.execute(query)
    mydb.commit()

#insert_picture('abc', 'def')

def insert_book(title, year, des, author_id, price, genre_id, publisher_id, picture_id):
    query = "INSERT INTO book_pj.books (title, published_year, description, author_id, price, genre_id, publisher, picture_id, uploaded_time, last_updated)\
        VALUES ('%s', %s, '%s', %s, %s, %s, %s, '%s', NOW(), NOW());" %(title, year, des, author_id, price, genre_id, publisher_id, picture_id)
    mycursor.execute(query)
    mydb.commit()

#insert_book("Van_2", 2022, "abc", 1, 25000, 1, 1, 1)

def update_book(book_id, title, year, des, author_id, price, picture_id, status, genre_id):
    query = "UPDATE book_pj.books SET last_updated = NOW()"
    try:
        if title != "":
            query += ", title = '%s'" %(title)
        if year != "":
            query += ", published_year = %s" %(year)
        if des != "":
            query += ", description = '%s'" %(des)
        if author_id != "":
            query += ",  author_id = %s" %(author_id)
        if price != "":
            query += ", price = %s" %(price)
        if picture_id != "":
            query += ", picture_id = %s" %(picture_id)
        if status != "":
            query += ", status = '%s'" %(status)
        if genre_id != "":
            query += ", genre_id = %s" %(genre_id)
    finally:
        query += " WHERE book_id = %s;" %(book_id)
        mycursor.execute(query)
        mydb.commit()

#update_book(15, "Van_3", 2019, 'def', "", "", "", "Empty", 2)

def delete_book(book_id):
    query = "DELETE FROM book_pj.books WHERE book_id = %s;" %(book_id)
    mycursor.execute(query)
    mydb.commit()

#delete_book(16)

def sorting_book(from_year, to_year, author_id, from_price, to_price, genre_id):
    query = "SELECT books.title, books.published_year, books.description, author.name, books.price, genre.main_genre, genre.sub_genre, picture_url.main_picture_url, books.publisher \
         FROM book_pj.books JOIN book_pj.author ON books.author_id = author.author_id \
             JOIN book_pj.genre ON books.genre_id = genre.genre_id\
                 JOIN book_pj.picture_url ON books.picture_id = picture_url.picture_id \
                     WHERE 1=1 "
    try:
        if from_year and to_year != "":
            query += "AND (published_year BETWEEN %s AND %s)" %(from_year, to_year)
        if author_id != "":
            query += "AND books.author_id =  %s" %(author_id)
        if from_price and to_price != "":
            query += "AND (price BETWEEN %s AND %s)" %(from_price, to_price)
        if genre_id != "":
            query += "AND books.genre_id =  %s" %(genre_id)
    finally:
        query += ";"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for i in result:
            print(i)

#sorting_book("", "", "", "", "", "")

def like_book(user_id, book_id):
    query = "INSERT INTO book_pj.users_like_books (user_id, book_id) VALUES (%s, %s);" %(user_id, book_id)
    mycursor.execute(query)
    mydb.commit()
    print("Đã thích!")

#like_book(1, 18)

def liked_list(user_id):
    query = "SELECT books.title, books.published_year, books.price, picture_url.main_picture_url, users.phone \
        FROM book_pj.books JOIN book_pj.picture_url ON books.picture_id = picture_url.picture_id \
            JOIN book_pj.users ON books.publisher = users.user_id \
                WHERE users.user_id = %s" %(user_id)
    mycursor.execute(query)
    result = mycursor.fetchall()
    for i in result:
        print(i)

#liked_list(1)

def unlike(user_id, book_id):
    query = "DELETE FROM book_pj.users_like_books WHERE user_id = %s AND book_id = %s;" %(user_id, book_id)
    mycursor.execute(query)
    mydb.commit()
    print("Đã bỏ thích!")

#unlike(1, 18)