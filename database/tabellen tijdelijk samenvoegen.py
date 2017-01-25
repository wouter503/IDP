import psycopg2 as psy2
con = psy2.connect("dbname=dezorggroepdatabase user=postgres host=localhost password=donaldniek")
dbname = "dezorggroepdatabase"
cur = con.cursor()
cur.execute("select * from test3 union select * from test4")
for i in cur:
    print(i)
con.commit()
cur.close()
con.close()
