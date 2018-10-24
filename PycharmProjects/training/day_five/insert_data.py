import pymysql

db = pymysql.connect("localhost", "demo", "demo", "test")
cursor = db.cursor()
sql = "insert into pets(name, owner, age) values('%s', '%s', '%d')" % ('Mac', 'Mike', 20)
try:
    cursor.execute(sql)
    print ("Successfully inserted data into the table")
except:
    #Rollback / revert back in case there is any error
    db.rollback()
    print ("Rollbacked")
else:
    db.commit()
db.close()
print ("Connection disconnected from DB")