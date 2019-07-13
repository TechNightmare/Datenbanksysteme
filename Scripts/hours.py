import cx_Oracle
import numpy 
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pass

# get Connection
connection = cx_Oracle.connect("S865745", "student", "localhost/oracle")
cursor = connection.cursor()

print ("Database connection established")

sql = """SELECT to_char(aoldata.querydata.querytime,'HH24') as Tag,
count(to_char(aoldata.querydata.querytime,'HH24')) as Anzahl
FROM aoldata.querydata
WHERE aoldata.querydata.query like '%facebook%'
GROUP BY to_char(aoldata.querydata.querytime,'HH24')
ORDER BY to_char(aoldata.querydata.querytime,'HH24')
"""

cursor.execute(sql)

x = []
y = []

for row in cursor:
	x.append((int(row[0])))
	y.append((row[1]))
	print(row)

plt.style.use("dark_background")
fig, graph = plt.subplots(1,1)
fig.set_figheight(8)
fig.set_figwidth(12)
graph.set_title("Aktivitaet nach Stunden")
graph.set_xlabel("Stunde")
graph.set_ylabel("Anfragen")

graph.plot(x, y, color="darkgreen", linewidth = 2)
graph.axis([0,23, 0, 1300])
graph.xaxis.set_ticks(numpy.arange(0, 23, 1))
fig.savefig("AktivitaetStunden.PNG")

plt.show()
print ("Finished") 