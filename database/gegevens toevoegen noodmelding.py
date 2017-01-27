import psycopg2 as psy2
import datetime
con = psy2.connect("dbname=Zorggroep user=postgres host=172.24.1.1 password=admin")
dbname = "Zorggroep"
cur = con.cursor()
tijd = datetime.datetime.today()
nu_datum = tijd.strftime("%d %B %Y")
nu_tijd = tijd.strftime("%H:%M:%S")
print(nu_datum)
print(nu_tijd)
while True:
    nummer = int(input('nummer:'))
    if nummer > 50:
        print('er zijn maar 50 woningen')
        continue
    else:

        cur.execute("INSERT INTO noodmeldingen (datum, tijd, nummer) VALUES (%s, %s, %s)",
            (nu_datum, nu_tijd, nummer)
            )
    con.commit()
    break
cur.close()
con.close()
