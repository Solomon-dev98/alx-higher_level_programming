#!/usr/bin/python3
"""An implementation of a script that displays all values in the a table
    where name matches the argument"""
import sys
import MySQLdb


def filter_states_by_userInput():

    # connect to a database server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # establish a cursor for connection to the db
    cursor = db.cursor()

    # execute the query to display all the values in a states table
    query = """SELECT * FROM states
             WHERE name = BINARY '{}'
             ORDER BY id ASC""".format(sys.argv[4])
    cursor.execute(query)
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
    filter_states_by_userInput()
