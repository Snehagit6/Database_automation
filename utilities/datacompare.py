from Database_automation.utilities.structuring_data import excel_sheet_data,csv_data,table_data
from operator import itemgetter

def compare_source_target(name, param1, param2,s_key, t_key):
    row = 1
    sheet_name = name
    if sheet_name == 'files':
        param1 = csv_data(param1)
        param2 = csv_data(param2)
    elif sheet_name == 'database':
        param1 = table_data(param1)
        param2 = table_data(param2)
    param1 = sorted(param1, key=lambda i:i[s_key])
    # # Fast implementation:sorted(param1, key=itemgetter('BusinessID'))

    param2 = sorted(param2, key=lambda i:i[t_key])
    for i, j in zip(param1,param2):
        if len(param1) > len(param2):
            (param2.append(dict(zip(i.keys(), [None] * len(i.keys())))))
            print(param2)
        elif len(param1) < len(param2):
            (param1.append(dict(zip(param1.keys(), [None] * len(param2.keys())))))
        print(f"For Row:{row}")
        for key in i:
            if i[key] == j[key]:
                print("***Matched**Source value :{} Destination value:{} \t\t".format(i[key], j[key]))
            else:
                print("***Mismatched**Source value :{} Destination value:{} \t\t".format(i[key], j[key]))
        row += 1
        print("\n")