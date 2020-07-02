import cx_Oracle
import numpy 
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pass


connection = cx_Oracle.connect(username, password, "localhost/oracle")
cursor = connection.cursor()

print ("Database connection established")
# get Connection

sql = """SELECT to_char(aoldata.querydata.querytime,'DDD') as Tag,
count(to_char(aoldata.querydata.querytime,'DDD')) as Anzahl
FROM aoldata.querydata
WHERE aoldata.querydata.query like '%facebook%'
GROUP BY to_char(aoldata.querydata.querytime,'DDD')
ORDER BY to_char(aoldata.querydata.querytime,'DDD')"""

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
graph.set_title("Aktivitaet nach Tagen")
graph.set_xlabel("Tag")
graph.set_ylabel("Anfragen")

graph.plot(x, y, color="darkgreen", linewidth = 2)
graph.axis([60,151, 0, 700])
graph.xaxis.set_ticks(numpy.arange(60, 151, 5))

fig.savefig("AktivitaetTage.PNG")
plt.show()
    
print ("Finished") 
