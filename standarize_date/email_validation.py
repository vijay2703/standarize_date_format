import re
import json

regex = '(?<!\S)(?=.)(0|([1-9](\d*|\d{0,2}(,\d{3})*)))?(\.\d*[1-9])?(?!\S)'



def standard_email():
  regex1 = '^(?:\d+|\d{1,2},(?:\d{2},)*\d{3})(?:\.\d{2})?$'       #indian currency
  regex2 = '(?<!\S)(?=.)(0|([1-9](\d*|\d{0,2}(,\d{3})*)))?(\.\d*[1-9])?(?!\S)'   #(100,000, 999.999, 90.0009, 1,000,023.999, 0.111, .1110}
  regex3='^([1-9]\d*|0)(\.\d+)?$'
  list1=['vij 123,000','1.23','00.1','nitin give me my money 10.0 and 40.0','you are way to slow man','100000','dihd 10,20,2102','10,200','0.01']
  dict={}
  pk=0
  for i in list1:
    lst=[]
    for j in i.split():
        print(j)
        if re.search(regex1,j) or re.search(regex2,j) or re.search(regex3,j) :
            lst.append(j)
    dict[pk]=lst
    pk=pk+1
  return(dict)
column_name='emailAddress'
# format=10
file_name='date_json.json'
a=standard_email()
print(a)