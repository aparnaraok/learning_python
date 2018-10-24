import pymysql

db = pymysql.connect("localhost", "demo", "demo", "test")
cursor = db.cursor()
age = int(input("Enter the age"))
sql = "select * from pets where age < %d" % (age)
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        name = row[0]
        owner = row[1]
        print ("name = %s, owner = %s" %(name, owner))
except:
    print ("Error : unable to fetch data")

db.close()