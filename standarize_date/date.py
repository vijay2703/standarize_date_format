import json
from dateutil import parser

def standard_date(file_name,column_name,format):
  with open(file_name) as f:
    data = json.load(f)
  for i in data:
    d = parser.parse(i[column_name])
    if format==0:
      i[column_name] = d.strftime("%d")
    elif format==1:
      i[column_name] = d.strftime("%m")
    elif format==2:
      i[column_name] = d.strftime("%Y")
    elif format==4:
      i[column_name] = d.strftime("%d-%m")
    elif format==5:
      i[column_name] = d.strftime("%m-%Y")
    elif format==6:
      i[column_name] = d.strftime("%d-%m-%Y")
    elif format==7:
      i[column_name] = d.strftime("%Y-%m-%d")
    elif format==8:
      i[column_name] = d.strftime("%H:%M:%S")
    elif format==9:
      i[column_name] = d.strftime("%d-%m-%Y %H:%M:%S")
    elif format==10:
      i[column_name] = d.strftime("%d-%m-%Y %H:%M:%S.%f")
  return(data)
column_name='date'
format=10                                     #1->"%Y-%m-%d"   2->"%d-%m-%Y
file_name='date_json.json'
a=standard_date(file_name,column_name,format)
print(a)