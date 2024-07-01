#!/usr/bin/python3
"""An implementation of a script that lists all cities from a database"""

import sys
import MySQLdb


def list_cities():

    # connect to a mysql server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3]
    )

    # create a cursor to interact wit the database
    cursor = db.cursor()

    # execute the query using parameterization
    query = """SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC"""
    cursor.execute((query),)

    # fetch all cities
    cities = cursor.fetchall()

    # print all cities
    for city in cities:
        print(city)

    # Close connections
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities()
