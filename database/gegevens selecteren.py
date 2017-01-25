import psycopg2 as psy2
con = psy2.connect("dbname=dezorggroepdatabase user=postgres host=localhost password=donaldniek")
dbname = "dezorggroepdatabase"
cur = con.cursor()
psy2.extensions.register_type(psy2.extensions.UNICODE, cur)
cur.execute("SELECT * FROM test2 where num = 200 and data = 'abcd'")
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
print('------------------------------------')
cur.execute("SELECT  count(id) FROM test2")  # min(id), avg(id), sum(id)
for i in cur:
    print(i)
print('------------------------------------')
cur.execute("SELECT * FROM test2 order by num asc, id desc")
for i in cur:
    print(i)
con.commit()
cur.close()
con.close()
