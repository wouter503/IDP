import psycopg2 as psy2
con = psy2.connect("dbname=dezorggroepdatabase user=postgres host=localhost password=donaldniek")
dbname = "dezorggroepdatabase"
cur = con.cursor()
cur.execute("INSERT INTO test2 (num, data) VALUES (%s, %s)",
            (225121, "abcd"))
con.commit()
cur.close()
con.close()
