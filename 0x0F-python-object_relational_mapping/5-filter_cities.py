#!/usr/bin/python3
"""Implementtion of a script that takes in the name of a state as an
argument and lists all cities of that state, using the database
hbtn_0e_4_usa"""
import sys
import MySQLdb


def filter_stateName():

    # connect to a database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3]
    )

    # establish a cursor for manipulating the db
    cursor = db.cursor()

    # execute the query and prevent sql injection
    query = """SELECT cities.id, cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC"""
    cursor.execute(query, (sys.argv[4],))

    # fetch and print all cities
    cities = cursor.fetchall()

    city_names = [city[1] for city in cities]
    print(", ".join(city_names))

    # close connections
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_stateName()
