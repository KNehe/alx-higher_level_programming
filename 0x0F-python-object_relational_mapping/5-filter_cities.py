#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_0_usa
Takes 4 arguments: mysql username, mysql password, database name,
and name of state
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    state = sys.argv[4]
    cur.execute("SELECT cities.name\
                FROM cities INNER JOIN states on cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id", (state, ))
    res = []
    for row in cur.fetchall():
        res.append(row[0])
    print(", ".join(res))
