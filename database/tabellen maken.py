import psycopg2 as psy2

con = psy2.connect("dbname=dezorggroepdatabase user=postgres host=localhost password=donaldniek")
dbname = "dezorggroepdatabase"
cur = con.cursor()
cur.execute("CREATE TABLE test4 (id serial PRIMARY KEY, flatnum integer, geg varchar);")
con.commit()
cur.close()
con.close()
