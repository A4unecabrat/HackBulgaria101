import sqlite3

""" conn = sqlite3.connect("polyglot.db")
cursor = conn.cursor()

result = cursor.execute("SELECT id, language FROM languages")

for row in result:
    print(row)
"""
data = [("Ivan Ivanov", 5000, 10000, "Software Developer"),
        ("Rado Rado", 500, 0, "Technical Support Intern"),
        ("Ivo Ivo", 10000, 100000, "CEO"),
        ("Petar Petrov", 3000, 1000, "Marketing Manager"),
        ("Maria Georgieva", 8000, 10000, "COO")]

db = sqlite3.connect('positions_hack')
db.execute('''
    CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, monthly_salary
     INTEGER, yearly_bonus INTEGER, position TEXT)
''')

db.executemany(''' INSERT INTO employees(name, monthly_salary, yearly_bonus,
 position) VALUES(?,?,?,?)''', data)

db.commit()
