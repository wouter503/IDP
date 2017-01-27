import psycopg2 as psy2
con = psy2.connect("dbname=Zorggroep user=postgres host=172.24.1.1 password=admin")
dbname = "Zorggroep"
cur = con.cursor()
psy2.extensions.register_type(psy2.extensions.UNICODE, cur)
""""cur.execute("SELECT * FROM ___ where ___ and ___ = ___")
for i in cur:
    print(i)
print('------------------------------------')
cur.execute("SELECT * FROM test2")

for i in cur:
    print(i)
print('------------------------------------')
cur.execute("SELECT  distinct num FROM test2")
for i in cur:
    print(i)
print('------------------------------------')"""""
cur.execute("SELECT  count(nummer) FROM noodmeldingen where nummer = 8")  # min(id), avg(id), sum(id)
for i in cur:
    print(i)
""""print('------------------------------------')
cur.execute("SELECT * FROM test2 order by num asc, id desc")
for i in cur:
    print(i)"""""
con.commit()
cur.close()
con.close()
