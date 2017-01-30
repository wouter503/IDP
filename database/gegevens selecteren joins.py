import psycopg2 as psy2
con = psy2.connect("dbname=Zorggroep user=postgres host=172.24.1.1 password=admin")
dbname = "Zorggroep"
cur = con.cursor()
psy2.extensions.register_type(psy2.extensions.UNICODE, cur)
# inner join
cur.execute("SELECT * FROM test, test2 where test.woning = test2.id")
for i in cur:
    print(i)
print('---------------------------------------------------------------------------')
# left outer join of right outer join
cur.execute("SELECT * FROM test2, test where test2.id = test.woning")
for i in cur:
    print(i)
con.commit()
cur.close()
con.close()
