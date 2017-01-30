import psycopg2 as psy2
con = psy2.connect("dbname=Zorggroep user=postgres host=172.24.1.1 password=admin")
dbname = "Zorggroep"
cur = con.cursor()
cur.execute("INSERT INTO woning (nummer) VALUES (50)"
            )
con.commit()
cur.close()
con.close()
