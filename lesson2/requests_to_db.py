import sqlite3

con = sqlite3.connect("../films.db")
cur = con.cursor()

category_id = 2
query1 = cur.execute(f"""SELECT * FROM Category WHERE id = {category_id}""")
result1 = query1.fetchone()
print(result1)

query2 = cur.execute(f"""SELECT * FROM Category WHERE id = ?""",
                     [category_id])
result2 = query2.fetchone()
print(result2)

query3 = cur.execute(f"""SELECT * FROM Category""")
result3 = query3.fetchall()
print(result3)

category_name = "вщхзфхзывщфзхывщ"

query4 = cur.execute(f"""INSERT INTO Category (title) VALUES ("{category_name}")""")
con.commit()
print("insert into!")

query4_5 = cur.execute(f"""SELECT id FROM Category WHERE title = ?""",
                       [category_name])
result4_5 = query4_5.fetchone()
category_id = result4_5[0]

query5 = cur.execute(f'''UPDATE Category 
SET title = "3467583654"
WHERE id = "{category_id}"''')
print("updated!")
con.commit()

query6 = cur.execute(f"""DELETE FROM Category WHERE id = {category_id}""")
print("deleted!")
con.commit()
#cur.close()
con.close()


