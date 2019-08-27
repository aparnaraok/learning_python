import MySQLdb

# Connect to MySQL Database
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="Starangel@9", db="oms")
cur = db.cursor()
