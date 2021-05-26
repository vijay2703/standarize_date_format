import re
import json

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def standard_email(file_name,column_name):
  regex = '^((\+\d{1,3}(-| )?\(?\d\)?(-| )?\d{1,3})|(\(?\d{2,3}\)?))(-| )?(\d{3,4})(-| )?(\d{4})(( x| ext)\d{1,5}){0,1}$'
  with open(file_name) as f:
    data = json.load(f)
  for i in data:
    if re.search(regex,i[column_name]):
        continue
    else:
        i[column_name]=None
  return(data)
column_name='phoneNumber'
# format=10                                     #1->"%Y-%m-%d"   2->"%d-%m-%Y
file_name='date_json.json'
a=standard_email(file_name,column_name)
print(a)