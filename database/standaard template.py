import psycopg2 as psy2
con = psy2.connect("dbname=dezorggroepdatabase user=postgres host=localhost password=donaldniek")
dbname = "dezorggroepdatabase"
cur = con.cursor()
#
con.commit()
cur.close()
con.close()
