#!/usr/bin/python3
import MySQLdb
import sys
"""
lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    MY_HOST = "localhost"
    MY_DB = sys.argv[3]
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]

    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS,
                         db=MY_DB)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE `name` LIKE "N%"'
                + ' ORDER BY `id` ASC')
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
