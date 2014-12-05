from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import random

Base = declarative_base()


class Players(Base):
    __tablename__ = "Players"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

engine = create_engine("sqlite:///Do_you_even_math.db")
Base.metadata.create_all(engine)

session = Session(bind=engine)
session.add_all([
    Players(name="The Hunger Games: Catching Fire", score=5),
    Players(name="Wreck-It Ralph", score=6),
    Players(name="Her", score=7)])
session.commit()

def calculatescore(number):
    return number * number


def question(score):
    operation = random.randint(1, 5)
    first_number = random.randrange(1, 1000)
    second_number = random.randrange(1, 1000)
    if operation == 1:
        print("what is the answer to {} + {}".format(first_number,
                                                     second_number))
        answer = input()
        if float(answer) == first_number + second_number:
            score += 1
        else:
            return calculatescore(score)
    elif operation == 2:
        print("what is the answer to {} - {}".format(first_number,
                                                     second_number))
        answer = input()
        if float(answer) == first_number - second_number:
            score += 1
        else:
            return calculatescore(score)
    elif operation == 3:
        print("what is the answer to {} * {}".format(first_number,
                                                     second_number))
        answer = input()
        if float(answer) == first_number * second_number:
            score += 1
        else:
            return calculatescore(score)
    elif operation == 4:
        print("what is the answer to {} / {}".format(first_number,
                                                     second_number))
        answer = input()
        if float(answer) == first_number / second_number:
            score += 1
        else:
            return calculatescore(score)
    else:
        print("what is the answer to {}^{}".format(first_number,
                                                   second_number))
        answer = input()
        if float(answer) == first_number ^ second_number:
            score += 1
        else:
            return calculatescore(score)


def main():
    while True:
        print("Here are you options for the game:")
        print("> Start a game")
        print("> Highscores")
        action = input("What do you want to do?")
        if action == "Highscores":
            session = Session(bind=engine)
            players = session.query(Players).order_by(Players.score).all()
if __name__ == '__main__':
    main()
