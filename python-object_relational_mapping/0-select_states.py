#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor
    cur = db.cursor()

    # Execute query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print results
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
