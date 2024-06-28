#!/usr/bin/python3
"""implementation of a script that takes in arguments and displays all
    values in the states table where name matches the argument"""
import sys
import MySQLdb


def sql_injection_safe():

    # connect ato a mysql server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    # establish a cursor for connection to the database
    cursor = db.cursor()

    # write and execute the query
    stateName = sys.argv[4]
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (stateName,))

    # Fetch all results
    all_states = cursor.fetchall()

    # print all states
    for st in all_states:
        print(st)

    # close connections
    cursor.close()
    db.close()


if __name__ == "__main__":
    sql_injection_safe()
