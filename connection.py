import pymysql

db=mysql.connect(host="localhost",user="admin",password="123456",database="205CDE")
cursor=db.cursor();

sql_query="SELECT VERSION()"

try:
	cursor.execute(sql_query)
	data=cursor.fetchone()
	print("database Version :%s" %data)

except Exception as e:
	print("Exception :", e):

	connection.close()