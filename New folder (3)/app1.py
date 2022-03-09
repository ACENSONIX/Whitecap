import mysql.connector
import webbrowser
from flask import json

conn = mysql.connector.connect(user='root', password='highflyer123',
                              host='localhost',database='whitecaps')

if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")

select = """SELECT * FROM patient"""
cursor = conn.cursor()
cursor.execute(select)
result = cursor.fetchall()

p = []

tbl = "<tr><th>FirstName</th><th>LastName</th><th>PatID</th><th>BloodGroup</th><th>Age</th><th>Gender</th><th>Location</th><th>Medical Comp.</th><th>Email</th><th>Phone</th></tr>"
p.append(tbl)

for row in result:
    for i in range(len(row)):
        if(i==11):
            continue
        else:

            a = "<td>%s</td>"%row[i]
            p.append(a)
    

from django.utils import simplejson
json_list = simplejson.dumps(p)
render_to_response("webbrowser.html", {'json_list': json_list})


