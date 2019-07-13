import cx_Oracle
import numpy 
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pass

print ("Database connection established")

# get Connection
connection = cx_Oracle.connect("S865745", "student", "localhost/oracle")
cursor = connection.cursor()

y = []
sum = 0

sql1 = """SELECT count(DISTINCT anonid)
FROM aoldata.querydata
WHERE clickurl LIKE '%facebook.com%'
ORDER BY anonid
"""

cursor.execute(sql1)


for row in cursor:
	print(row[0])
	sum = row[0]

sql2 = """SELECT COUNT(fbuser.anonid)
FROM FBUser
INNER JOIN MySpaceUser ON fbuser.anonid = myspaceuser.anonid
"""

cursor.execute(sql2)

for row in cursor:
	print(row[0])
	sum -= row[0]
	y.append(row[0])

sql3 = """SELECT COUNT(fbuser.anonid)
FROM FBUser
INNER JOIN flickruser ON fbuser.anonid = flickruser.anonid
"""

cursor.execute(sql3)

for row in cursor:
	print(row[0])
	sum -= row[0]
	y.append(row[0])

sql4 = """SELECT COUNT(fbuser.anonid)
FROM FBUser
INNER JOIN youtubeuser ON fbuser.anonid = youtubeuser.anonid
"""

cursor.execute(sql4)

for row in cursor:
	print(row[0])
	sum -= row[0]
	y.append(row[0])

y.append(sum)		#onlyFBNutzer

objects = "MySpace", "Flickr", "Youtube", "nur Facebook"

plt.style.use("dark_background")
colors = ["lightseagreen", "orchid", "red", "royalblue"]
explode = (0.1, 0, 0, 0)  #hervorstellen

plt.pie(y, explode = explode, labels = objects, colors = colors, autopct = "%1.1f%%", shadow = True, startangle = 0)
plt.axis("equal")
plt.title("Facebook User in anderen sozialen Netzwerken")
plt.savefig("fbuserothernetworks.PNG",)
plt.show()
   
print ("Finished") 