# import re
# print(re.finditer(r'From\s+', 'Fromage amk'))
f_text=open('abbreviation.txt','r')
# print(f_text.readline()
lst=[]
dict={}
for i in f_text:
    lst=lst+i.split()
print(lst)
    # dict[i[0]]=i[1]
for j in range(len(lst)-1):
    if j%2==0:
        dict[lst[j]]=lst[j+1]
# print(dict)
list_abb2=[dict]
print(list_abb2)