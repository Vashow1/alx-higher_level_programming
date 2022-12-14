#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    MY_HOST = "localhost"

    db = MySQLdb.connect(host=MY_HOST, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()

    cur.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name` "
                + "FROM `cities` " +
                "INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`"
                + " ORDER BY `cities`.`id` ASC")
    [print(row) for row in cur.fetchall()]
    cur.close()
    db.close()
