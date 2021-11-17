import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="123456",
database="store_cms_plusplus"
)

mycursor = mydb.cursor()

class Statistic:
    def __init__(self, maker, sold, totalMoney):
        self.maker = maker
        self.sold = sold
        self.totalMoney = totalMoney
    def __str__(self):
        return "Hãng: %s, Số lượng: %s, Số tiền: %s" % (self.maker, self.sold, self.totalMoney)

def getStatisticbyMaker():
    mycursor.execute(f"SELECT maker, sold, (sold * price) FROM store_cms_plusplus.laptop GROUP BY maker ORDER BY maker ASC;")
    result = mycursor.fetchall()
    result_list = []
    for i in result:
        stat = Statistic(i[0], i[1], i[2])
        result_list.append(stat)
    return result_list

for i in getStatisticbyMaker():
    print(i)