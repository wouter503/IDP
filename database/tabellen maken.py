import psycopg2 as psy2
con = psy2.connect("dbname=Zorggroep user=postgres host=172.24.1.1 password=admin")
dbname = "Zorggroep"
cur = con.cursor()
cur.execute("CREATE TABLE test (datum date not null, tijd time not null, primary key(datum,tijd), nummer integer references woning(nummer));")
con.commit()
cur.close()
con.close()
