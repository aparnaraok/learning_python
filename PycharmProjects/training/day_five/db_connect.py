#!/usr/bin/env python

import pymysql
print ("Successfully imported pymysql")

#Open database connection
db = pymysql.connect("localhost", "demo", "demo", "test")

#Prepare a cursor object using cursor() method
cursor = db.cursor()

#Execute SQL query using execute method
cursor.execute("SELECT VERSION()")

#fetch a single row using fetchone() method
data = cursor.fetchone()

print ("Database version  :  : %s"  %data)

#Disconnect from server
db.close()