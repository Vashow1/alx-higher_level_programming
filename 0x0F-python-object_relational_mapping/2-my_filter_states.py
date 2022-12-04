#!/usr/bin/python3
"""
takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name
matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    user_in = sys.argv[4]

    db = MySQLdb.connect(host=MY_HOST, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`" +
                " WHERE BINARY `name` = '{}'".format(user_in) +
                " ORDER BY `id` ASC")
    [print(row) for row in cur.fetchall()]
