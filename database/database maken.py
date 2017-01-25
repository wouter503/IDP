from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

con = connect("user=postgres host=localhost password=donaldniek")

dbname = "abcd"

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
cur.execute('CREATE DATABASE ' + dbname)
cur.close()
con.close()
