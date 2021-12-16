#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_0_usa
Takes 3 arguments: mysql username, mysql password, database name
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states on cities.state_id = states.id\
                ORDER BY cities.id")
    for row in cur.fetchall():
        print(row)
