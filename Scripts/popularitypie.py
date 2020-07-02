import cx_Oracle
import numpy 
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pass

print ("Database connection established")

# get Connection
connection = cx_Oracle.connect(username, password, "localhost/oracle")
cursor = connection.cursor()

y = []

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

objects = "MySpace", "Flickr", "Youtube", "Facebook", "Friendster"

colors = ["lightseagreen", "orchid", "red", "royalblue", "gold"]
explode = (0, 0, 0, 0.2, 0)  #hervorstellen

plt.style.use("dark_background")
plt.pie(y, explode = explode, labels = objects, colors = colors, autopct = "%1.1f%%", shadow = True, startangle = 0)
plt.axis("equal")
plt.title("Nutzerverteilung")
plt.savefig("NutzerzahlenPie.PNG",)
plt.show()
   
print ("Finished") 
