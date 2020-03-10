import csv
import json

####################################################################

# Here you can change the CSV file:

file_csv = 'csv_input.csv'

####################################################################

def print_csv(data):
    ret = ""
    for row in data:
        for element in row:
            print(element)
        print("\n")
    return str(ret)

def json_generator_by_csv(data, curr_lvl, father, curr_num_brothers):
    ret=""
    count_brother = 0
    for row in data:
        if str(curr_lvl)==str(row[0]) and str(father)==str(row[4]):
            count_brother+=1
            ret += '{'
            ret += '"title": "'+row[1]+'",'
            ret += '"icon": "'+row[2]+'"'
            if str(row[3]) != str(None):
                num_brothers = str(row[3]).count(",")
                ret += ', "child":['
                ret += json_generator_by_csv(data, curr_lvl+1, row[1], num_brothers)
                ret += ']'
            ret += "}"
            if int(count_brother)<=int(curr_num_brothers):
                ret+=","
    return str(ret)

with open(file_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = list(csv_reader)
    data.pop(0)
    print_csv(data)
    num_lvl0 = -1
    for row in data:
        if int(row[0])==0:
            num_lvl0+=1
    if num_lvl0>=0:
        str_json_menu = json_generator_by_csv(data, 0, None, num_lvl0)
        str_final = '{ "menu":['+str_json_menu+'] }'
        #menu_in_json_format = json.loads(str_json_menu)
        data_file = open("json_output.json", "w")
        with data_file as f:
            f.write(str_final)
        data_file.close()
