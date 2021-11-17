import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="123456",
database="store_cms_plusplus"
)

mycursor = mydb.cursor()

class Counter:
    def __init__(self, maker, quantity):
        self.maker = maker
        self.quantity = quantity
    def __str__(self):
        return "Maker: %s, Quantity: %s" % (self.maker, self.quantity)

def getCounterbyMaker():
    mycursor.execute(f"SELECT maker, COUNT(maker) as 'quantity' FROM store_cms_plusplus.laptop GROUP BY maker ORDER BY quantity DESC;")
    result = mycursor.fetchall()
    result_list = []
    for x in result:
        counter = Counter(x[0], x[1])
        result_list.append(counter)
    print(result_list)
    for x in result_list:
        print(x)

getCounterbyMaker()