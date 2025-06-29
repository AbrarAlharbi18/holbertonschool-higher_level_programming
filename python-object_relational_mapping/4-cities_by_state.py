#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa:
"""
import sys
from MySQLdb import connect

if __name__ == "__main__":
    arg = sys.argv
    username = arg[1]
    passwd = arg[2]
    db = arg[3]          # database name
    for name in arg:    # input validation to check injection
        if ";" in name:
            validate = False
        else:
            validate = True
    if len(arg) == 4 and validate is True:
        with connect(
                host="localhost", user=username,
                password=passwd, database=db,
                port=3306
                ) as mysql_db:
            cursor = mysql_db.cursor()
            cursor.execute(
                    """
                    SELECT cities.id, cities.name, states.name FROM cities
                    INNER JOIN states ON cities.state_id = states.id
                    """
                    )
            result = cursor.fetchall()
            for i in result:
                print(i)
