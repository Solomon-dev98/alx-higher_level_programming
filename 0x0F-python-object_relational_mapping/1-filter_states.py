#!/usr/bin/python3
""" A implementation of a function that lists all state starting with N
    from aa database"""
import sys
import MySQLdb


def filter_states():

    # connect to a mysql server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # establish a cursor to interact with the database
    cursor = db.cursor()

    # execute the query to retrieve states starting with N
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # fetch all the staes starting with N
    states = cursor.fetchall()

    # print all the states
    for state in states:
        print(state)

    # close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    filter_states()
