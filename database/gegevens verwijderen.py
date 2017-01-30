import psycopg2 as psy2
con = psy2.connect("dbname=Zorggroep user=postgres host=172.24.1.1 password=admin")
dbname = "Zorggroep"
cur = con.cursor()
psy2.extensions.register_type(psy2.extensions.UNICODE, cur)
cur.execute("DELETE from noodmeldingen where nummer = 8")
cur.execute("SELECT * FROM noodmeldingen")
for i in cur:
    print(i)
con.commit()
cur.close()
con.close()
