import psycopg2 as psy2
con = psy2.connect("dbname=dezorggroepdatabase user=postgres host=localhost password=donaldniek")
dbname = "dezorggroepdatabase"
cur = con.cursor()
psy2.extensions.register_type(psy2.extensions.UNICODE, cur)
cur.execute("update test2 set num = 300 where id = 2")
cur.execute("SELECT * FROM test2")
for i in cur:
    print(i)
con.commit()
cur.close()
con.close()
