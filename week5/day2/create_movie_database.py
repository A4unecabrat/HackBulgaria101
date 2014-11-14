import sqlite3

data1 = [("The Hunger Games: Catching Fire", 7.9),
         ("Wreck-It Ralph", 7.8),
         ("Her", 8.3)]

data2 = [(1, "3D", "2014-04-01", "19:10"),
         (1, "2D", "2014-04-01", "19:00"),
         (1, "4DX", "2014-04-02", "21:00"),
         (3, "2D", "2014-04-05", "20:20"),
         (2, "3D", "2014-04-02", "22:00"),
         (2, "2D", "2014-04-02", "19:30")]

data3 = [("RadoRado", 1, 2, 1),
         ("RadoRado", 1, 3, 5),
         ("RadoRado", 1, 7, 5),
         ("Ivo", 3, 1, 1),
         ("Ivo", 3, 1, 2),
         ("Mysterious", 5, 2, 3),
         ("Mysterious", 5, 2, 4)]
db = sqlite3.connect("Movies_database")
db.execute(
    '''CREATE TABLE Movies(id INTEGER PRIMARY KEY, name TEXT, rating REAL)''')
db.executemany(''' INSERT INTO Movies(name, rating) VALUES(?,?)''', data1)


db.execute(
    '''CREATE TABLE Projections(id INTEGER PRIMARY KEY,movie_id INTEGER, type TEXT, date TEXT, time TEXT)''')
db.executemany(
    ''' INSERT INTO Projections(movie_id, type, date, time) VALUES(?,?,?,?)''', data2)

db.execute(
    '''CREATE TABLE Reservations(id INTEGER PRIMARY KEY, username TEXT, projection_id INTEGER, row INTEGER, col INTEGER)''')
db.executemany(
    ''' INSERT INTO Reservations(username, projection_id, row, col) VALUES(?,?,?,?)''', data3)
