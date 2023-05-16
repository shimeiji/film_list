import sqlite3


connection = sqlite3.connect("test.db")
cursor = connection.cursor()

#cursor.execute("create table people (name text, marital_status text, age integer)")
 
test_list = [
	("Andy", "single", 21),
	("Pattie", "married", 34),
	("Julie", "single", 15),
	("Charlie", "divorced", 66),
	("Angelina", "divorced", 43)
]


#cursor.executemany("insert into people values (?,?,?)", test_list)
#cursor.execute("select * from people")
cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
test_search = cursor.fetchall()
print(test_search)


connection.commit()
connection.close()