# Make sure pandas is loaded
import pandas as pd
import os
import pytz
import json
from datetime import datetime,timezone
surveys_df = pd.read_csv('movies2.csv')
def csv_datatype(csv_file):
    column_name=list(csv_file.columns)
    # print("column name=>",column_name)
    csv_file=pd.DataFrame(csv_file)
    for df in csv_file:
        if csv_file[df].dtype== 'object':
            csv_file[df] = csv_file[df].astype('str')

    mask1 = csv_file.astype(str).apply(lambda x : x.str.match(r'\d{2}-\d{2}-\d{4}').all())                                 #dd-mm-yyyy
    csv_file.loc[:, mask1] = csv_file.loc[:, mask1].apply(pd.to_datetime)
    mask2 = csv_file.astype(str).apply(lambda x : x.str.match(r'\d{4}-\d{2}-\d{2}').all())                                 #yyyy-mm-dd
    csv_file.loc[:, mask2] = csv_file.loc[:, mask2].apply(pd.to_datetime)
    mask3 = csv_file.astype(str).apply(lambda x : x.str.match(r'\d{2}/\d{2}/\d{4}').all())                                 #yyyy/mm/dd
    csv_file.loc[:, mask3] = csv_file.loc[:, mask3].apply(pd.to_datetime)
    mask4 = csv_file.astype(str).apply(lambda x : x.str.match(r'\d{2}/\d{2}/\d{4}').all())                                 #dd/mm/yyyy
    csv_file.loc[:, mask4] = csv_file.loc[:, mask4].apply(pd.to_datetime)
    mask5 = csv_file.astype(str).apply(lambda x : x.str.match(r'\d{2}-\d{2}-\d{4} \d{2}\:\d{2}\:\d{2}').all())             #dd-mm-yyyy hh:mm:ss
    csv_file.loc[:, mask5] = csv_file.loc[:, mask5].apply(pd.to_datetime)
    mask6 = csv_file.astype(str).apply(lambda x : x.str.match(r'\d{4}-\d{2}-\d{2} \d{2}\:\d{2}\:\d{2}').all())             #yyyy-mm-dd hh:mm:ss
    csv_file.loc[:, mask6] = csv_file.loc[:, mask6].apply(pd.to_datetime)
    mask7 = csv_file.astype(str).apply(lambda x : x.str.match(r'\d{4}/\d{2}/\d{2} \d{2}\:\d{2}\:\d{2}').all())             #yyyy/mm/dd hh:mm:ss
    csv_file.loc[:, mask7] = csv_file.loc[:, mask7].apply(pd.to_datetime)
    mask8 = csv_file.astype(str).apply(lambda x : x.str.match(r'\d{2}-\d{2}-\d{4} \d{2}\:\d{2}\:\d{2}').all())             #dd/mm/yyyy hh:mm:ss
    csv_file.loc[:, mask8] = csv_file.loc[:, mask8].apply(pd.to_datetime)
    mask9 = csv_file.astype(str).apply(lambda x : x.str.match(r'\d{2}\:\d{2}\:\d{2}').all())                               #hh:mm:ss
    csv_file.loc[:, mask9] = csv_file.loc[:, mask9].apply(pd.to_datetime)
    mask10 = csv_file.astype(str).apply(lambda x : x.str.match(r'\d{2}-\d{2}-\d{4} \d{2}\:\d{2}\:\d{2}-\d{2}').all())      #dd-mm-yyyy hh:mm:ss-tz
    csv_file.loc[:, mask10] = csv_file.loc[:, mask10].apply(pd.to_datetime)

    data_type=csv_file.dtypes
    data_type=pd.Series(data_type).tolist()                     #data type stored in list
    dict_csv={}
    tup_csv=()
    for i in range(len(data_type)):
        #print(data_type[i])
        if data_type[i]=='object':
            data_type[i]='TEXT'
        elif data_type[i]=='int64':
            data_type[i]='BIGINT'
        elif data_type[i]=='float64':
            data_type[i]='float'
        elif data_type[i]=='bool':
            data_type[i]='bool'
        # elif data_type[i]=='category':
        #     data_type[i]='category'
        elif data_type[i]=='bool':
            data_type[i]='bool'
        # elif data_type[i]=='datetime64[ns, pytz.FixedOffset(-420)]':
        #     data_type[i]='timestamptz'
        elif data_type[i] == 'datetime64[ns]':
            data_type[i] = 'timestamp'
        else:
            data_type[i] = 'timestamptz'
        dict_csv[column_name[i]]=data_type[i]
        tup_csv=tup_csv+("{a} {b}".format(a=column_name[i],b=data_type[i]),)
    # print("dictionary=>",dict_csv)
    # print("tuple=>",tup_csv)
    return(dict_csv,tup_csv)

a,b=csv_datatype(surveys_df)
print(a,b)