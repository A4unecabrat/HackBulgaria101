import sqlite3
db = sqlite3.connect("Movies_database")


def show_movies():
    list_of_movies = db.execute(
        '''SELECT name, rating FROM Movies ORDER BY rating desc''')
    for row in list_of_movies:
        print("{}-{}".format(row[0], row[1]))
    db.commit()


def show_movie_projections(movie_id, date_id):
    if date_id == "0":
        list_of_porjections = db.execute(
            '''SELECT date, time, type FROM Projections WHERE movie_id = ?ORDER BY date ''', (movie_id,))
        movie = db.execute(
            '''SELECT name FROM Movies WHERE id = ?''', (movie_id,))
        print("Projections for movie '{}'".format(movie[0]))
        for row in list_of_porjections:
            print("{} {} {}".format(row[0], row[1], row[2]))
    else:
        list_of_porjections = db.execute(
            '''SELECT date, time, type FROM Projections WHERE date = ?''', (date_id))
        movie = db.execute(
            '''SELECT name FROM Movies WHERE id = ?''', (movie_id,))
        print(movie[0])
        for row in list_of_porjections:
            print("{} {} {}".format(row[0], row[1], row[2]))


def main():
    command = ""
    while command != "exit":
        command = input("what the fuck do you want bitch? ")
        if command == "show movies":
            show_movies()
        elif command == "show movie projections":
            movie_id = input("select a movie id: ")
            date_id = input("so you want a date? if no enter 0: ")
            show_movie_projections(movie_id, date_id)
    db.close()
if __name__ == '__main__':
    main()
