import sqlite3

#databse connection
con = sqlite3.connect("mpms.db")
#con = sqlite3.connect("mpms_login.db")
cursor = con.cursor()

#Tables
#cursor.execute("CREATE TABLE admin(id INTEGER PRIMARY KEY, username VARCHAR(100), password VARCHAR(100))")
#cursor.execute("CREATE TABLE admin_curr_status (id INTEGER PRIMARY KEY, behaviour DATETIME DEFAULT CURRENT_TIMESTAMP, status TINYINT(1), aid INT)")
#cursor.execute("CREATE TABLE workers_data (id INTEGER PRIMARY KEY, creation_date DATETIME, nic VARCHAR(11), name VARCHAR(50), cdid INTEGER, pNumber VARCHAR(10), age INTEGER(10), address VARCHAR(100), sex TINYINT(1),payment VARCHAR(10) DEFAULT 'Not Paied',paied_time DATETIME DEFAULT 0)")
#cursor.execute("CREATE TABLE company (id INTEGER PRIMARY KEY, company_name VARCHAR(50), date_of_add DATETIME)")
#cursor.execute("CREATE TABLE department (id INTEGER PRIMARY KEY,company_name VARCHAR(50), department_name VARCHAR(50),creation_date DATETIME)")
#cursor.execute("CREATE TABLE working_details (id INTEGER PRIMARY KEY,company_name VARCHAR(50),department_name VARCHAR(50),payment INTEGER,workers_count INTEGER,enrolled_workers INTEGER DEFAULT 0,creation_date DATE)")


#Inserting Data
#cursor.execute("INSERT INTO admin (username, password) VALUES (:username, :password)",{'username':username, 'password':password})
#cursor.execute("INSERT INTO admin_curr_status (status,aid) VALUES (:bitt, :aid)",{'bitt':bitt, 'aid':aid})
#cursor.execute("INSERT INTO company (company_name) VALUES ('Brandix Lingerie')")
#cursor.execute("INSERT INTO working_details (company_name,department_name,payment,workers_count,creation_date) VALUES ('d','d',1500,12,'12/31/01')")

#Other Queries
#cursor.execute("SELECT * FROM working_details")
#cursor.execute("DROP TABLE workers_data")
cursor.execute("DELETE FROM workers_data")
cursor.execute("DELETE FROM working_details")
#cursor.execute("UPDATE company_department SET enrolled_workers = 8 WHERE cid = 1 and did = 2")
#cursor.execute("SELECT company_name,department_name,payment,workers_count,enrolled_workers FROM working_details WHERE company_name = 'Hemas' and department_name = 'Dep1'")

"""
register_company = 'Lalan Gloves'
register_department = 'Dep1'
e = 2
cursor.execute("SELECT department_name FROM department WHERE company_name = :x",{'x':register_company})
result = cursor.fetchall()
for x in result:
	print(x[0])
"""
con.commit()

con.close()