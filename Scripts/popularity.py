import cx_Oracle
import numpy 
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pass

# get Connection
connection = cx_Oracle.connect(username, password, "localhost/oracle")
cursor = connection.cursor()

print ("Database connection established")

y = []		#Were fuer Achse

sql1 = """SELECT count(DISTINCT anonid)
FROM aoldata.querydata
WHERE clickurl LIKE '%myspace.com%'
ORDER BY anonid
"""

cursor.execute(sql1)

for row in cursor:
	print(row[0])
	y.append(row[0])

sql2 = """SELECT count(DISTINCT anonid)
FROM aoldata.querydata
WHERE clickurl LIKE '%flickr.com%'
ORDER BY anonid
"""

cursor.execute(sql2)

for row in cursor:
	print(row[0])
	y.append(row[0])

sql3 = """SELECT count(DISTINCT anonid)
FROM aoldata.querydata
WHERE clickurl LIKE '%youtube.com%'
ORDER BY anonid
"""

cursor.execute(sql3)

for row in cursor:
	print(row[0])
	y.append(row[0])

sql4 = """SELECT count(DISTINCT anonid)
FROM aoldata.querydata
WHERE clickurl LIKE '%facebook.com%'
ORDER BY anonid
"""

cursor.execute(sql4)

for row in cursor:
	print(row[0])
	y.append(row[0])

sql5 = """SELECT count(DISTINCT anonid)
FROM aoldata.querydata
WHERE clickurl LIKE '%friendster.com%'
ORDER BY anonid
"""

cursor.execute(sql5)

for row in cursor:
	print(row[0])
	y.append(row[0])

objects = ("MySpace", "Flickr", "Youtube", "facebook", "Friendster")
y_pos = numpy.arange(len(objects))

plt.style.use("dark_background")
plt.bar(y_pos, y, align = "center", alpha = 0.5)
plt.xticks(y_pos, objects)
plt.ylabel("Nutzer")
plt.title("Nutzerzahlen sozialer Netzwerke")

plt.savefig("Nutzerzahlen.PNG",)
plt.show()
   
print ("Finished") 
