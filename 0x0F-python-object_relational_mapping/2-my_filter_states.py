#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa where name
matches the argument
Takes 4 arguments: mysql username, mysql password, database name,
and state name searched
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(sys.argv[4]))
    for row in cur.fetchall():
        print(row)
