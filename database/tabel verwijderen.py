import psycopg2 as psy2
con = psy2.connect("dbname=Zorggroep user=postgres host=172.24.1.1 password=admin")
dbname = "Zorggroep"
cur = con.cursor()
cur.execute("DROP TABLE woning")
con.commit()
cur.close()
con.close()
