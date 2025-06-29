#!/usr/bin/python3
"""Added a condition to prevent SQL injection."""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
    with MySQLdb.connect(
            host="localhost", user=username, passwd=password, db=database
            ) as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"\
            .format(search)
        if ";" not in search:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
