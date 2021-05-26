
import json
def bug_fixed(a):
    dict={}
    for i in a:
        dict[i['column_name']]=i['data_type']
    dict=json.dumps(dict)
    return dict


a=[{"column_name": "id", "data_type": "bigint"},{"column_name": "timestamp", "data_type": "timestamp without time zone"},{"column_name": "userstamp", "data_type": "character varying"},{"column_name": "descr", "data_type": "character varying"},{"column_name": "current_release", "data_type": "integer"},{"column_name": "full_descr", "data_type": "character varying"},{"column_name": "alive", "data_type": "character varying"},{"column_name": "for_release", "data_type": "character"},{"column_name": "display_name", "data_type": "character varying"},{"column_name": "project_id", "data_type": "character varying"},{"column_name": "avg_length", "data_type": "bigint"},{"column_name": "min_length", "data_type": "bigint"},{"column_name": "max_length", "data_type": "bigint"},{"column_name": "num_sequences", "data_type": "bigint"},{"column_name": "num_organisms", "data_type": "bigint"}]
l=bug_fixed(a)
print(l)