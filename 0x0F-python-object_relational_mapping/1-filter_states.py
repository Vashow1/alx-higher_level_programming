#!/usr/bin/python3
"""
lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
if __name__ == "__main__":
    MY_HOST = "localhost"
    MY_DB = sys.argv[3]
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]

    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS,
                         db=MY_DB)
    cur = db.cursor()
    cur.execute('SELECT * FROM states'
                + ' ORDER BY `id` ASC')
    [print(row) for row in cur.fetchall() if row[1][0] == 'N']
    cur.close()
    db.close()
