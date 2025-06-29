#!/usr/bin/python3
"""Lists all the cities associated with a state in the database."""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    with MySQLdb.connect(
            host="localhost", user=username, passwd=password, db=database
            ) as connection:
        cursor = connection.cursor()
        query = "SELECT cities.name FROM cities JOIN states\
            ON cities.state_id = states.id WHERE states.name = '{}'"\
            .format(state)
        if ";" not in state:
            cursor.execute(query)
            result = cursor.fetchall()
            cities = []
            for row in result:
                cities.append(row[0])
            output = ", ".join(cities)
            print(output)
