from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

con = connect("dbname=Zorggroep user=postgres host=172.24.1.1 password=admin")

dbname = "abcd"

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
cur.execute('drop DATABASE ' + dbname)
cur.close()
con.close()
