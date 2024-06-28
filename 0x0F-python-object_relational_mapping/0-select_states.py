#!/usr/bin/python3
""" A script that lists all the state from a database """
import sys
import MySQLdb


def select_states():
    """ a function that lists state from a database"""
    # read the three arguments from the commandline
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connect to a mysql server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # establish a cursor to communicate with the database
    cursor = db.cursor()

    # excute the query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch all the states
    states = cursor.fetchall()

    # print each state
    for state in states:
        print(state)

    # close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    select_states()
