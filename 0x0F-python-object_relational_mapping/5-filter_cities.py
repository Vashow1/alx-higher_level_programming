#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    user_in = sys.argv[4]
    MY_HOST = "localhost"

    db = MySQLdb.connect(host=MY_HOST, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()

    cur.execute("SELECT `cities`.`name` "
                + "FROM `cities` " +
                "INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`"
                " WHERE `states`.`name` = %s" 
                + " ORDER BY `cities`.`id` ASC", (user_in,))
    cities = ", ".join([row[0] for row in cur.fetchall()])
    print(cities)
    cur.close()
    db.close()
