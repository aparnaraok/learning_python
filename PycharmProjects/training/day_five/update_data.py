#import MySQLdb
import pymysql

#db = MySQLdb.connect("localhost","testuser","test123", "TESTDB")
db = pymysql.connect("localhost", "demo", "demo", "test")
cursor = db.cursor()
sql = "update pets set age = age + 1 where age > 12"

try:
    cursor.execute(sql)
    db.commit()
    print ("Update successful")
except:
    db.rollback()
db.close()