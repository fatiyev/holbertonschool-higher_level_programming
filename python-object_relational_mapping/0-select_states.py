#!/usr/bin/python3
"""Script that lists all states from database hbtn_0e_0_usa"""

import MySQLdb
import sys


def get_states():
    """Connects to MySQL and lists all states"""

    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")

    finally:
        try:
            cur.close()
            db.close()
        except Exception:
            pass


if __name__ == "__main__":
    get_states()
    