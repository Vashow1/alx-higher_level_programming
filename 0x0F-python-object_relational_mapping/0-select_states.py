#!/usr/bin/python3
import MySQLdb
import sys
"""
 lists all states from the database hbtn_0e_0_usa

"""
if __name__ == "__main__":
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_BASE = sys.argv[3]
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER,
                         passwd=MY_PASS, db=MY_BASE)
    curs = db.cursor()
    curs.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    for state in curs.fetchall():
        print(state)
