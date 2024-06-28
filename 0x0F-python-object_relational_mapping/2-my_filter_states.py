#!/usr/bin/python3
"""An immplementation of a script that displays all values in the a table
    where name matches the argument"""
import sys
import MySQLdb


def filter_states_by_userInput():

    # connect to a database server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # establish a cursor for connection to the db
    cursor = db.cursor()

    # execute the query to display all the values in a states table
    cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
                   .format(searched_state))
    # fetch the searched state
    states = cursor.fetchall()

    # print the searched state
    for state in states:
        print(state)

    # close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # read the command line args
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched_state = sys.argv[4]

    filter_states_by_userInput()
