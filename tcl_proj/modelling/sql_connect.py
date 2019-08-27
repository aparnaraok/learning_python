#import pymysql


#host  = "127.0.0.1"
#port = "3306"
#user = "root"
#password = "Starangel@9"

#db = pymysql.connect(host, port, user, password)
#print(db)

import pymysql

db = pymysql.connect(host="127.0.0.1", user="root", passwd="Starangel@9", db="oms")

cur = db.cursor()

cur.execute("SELECT * FROM `vw_order_vs_pe_rcmd_site_cmp_new`")

for row in cur.fetchall():
    print(row[1])

db.close()