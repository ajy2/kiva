import json
import time
import requests

base_url = 'https://api.kivaws.org/v1/loans/'

file = open('leaked_file_list1.txt', 'r', encoding='utf8');

for line in file:
    temp = line.split(',')

for idx, value in enumerate(temp):
    temp[idx] = value.strip();

for idx, value in enumerate(temp):
    file_name = value+'.json'
    r = requests.get(base_url+file_name)
    
    try:
        if(str(r)!='<Response [403]>'):
            print(str(idx) + " : " + str(r))

            path= './kiva_dataset/loan/'+file_name
            with open(path, 'w', encoding='utf-8') as make_file:
                json.dump(r.json(), make_file)
            time.sleep(1)
        else:
            print("taking a nap")
            time.sleep(1800)
            print(str(i) + " : " + str(r))

            path='./kiva_dataset/loan/'+file_name
            with open(path, 'w', encoding='utf-8') as make_file:
                json.dump(r.json(), make_file)
            time.sleep(1)
    except:
        pass
