import mysql.connector
#this is my database name and user pass
cnx = mysql.connector.connect(user= 'root', password= '', host= '127.0.0.1', database= 'employers')
cursor = cnx.cursor()
query = ('SELECT * FROM information')
cursor.execute(query)
all_info = dict()
for (name, weight, height) in cursor:
    every_info = {'weight': 0, 'height' : 0}
    every_info['weight'] = weight
    every_info['height'] = height
    all_info[name] = every_info
sorted_info = sorted(all_info, key=lambda k:(-all_info[k]['height'], all_info[k]['weight']))
for each_one in sorted_info:
    print('%s %i %i' %(each_one, all_info[each_one]['height'], all_info[each_one]['weight']))


cursor.close()
cnx.close()