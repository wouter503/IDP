import psycopg2 as psy2
con = psy2.connect("dbname=Zorggroep user=postgres host=172.24.1.1 password=admin")
dbname = "Zorggroep"
cur = con.cursor()
cur.execute("select * from woning union select * from noodmeldingen")
for i in cur:
    print(i)
con.commit()
cur.close()
con.close()
