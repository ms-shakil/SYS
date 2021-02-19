#!/usr/bin/env python3

import sys
import json

JSON_DATA = "./engineer.json"

ENGINEER_DATA =[]

def help_message():
    print("User:{},Program".format(PROGRAM))
    print("Opration and Programe")
    print("--help\t: usage message:")
    print("--h\t:usage message:")
    print(" ")
    print("Argument can be one of:")
    print("insert\t: enter an entry:")
    print("inset argument\t id, name,age,gender:")
    print("update\t: enter an entry:")
    print("update argument\t  id , key, new_value:")
    print("show\t: enter an entry:")
    print("update argument :\tid")
    print("delete\t enter an entery:")
    print("delete argument \t id")

def read_json():
    global ENGINEER_DATA
    with open(JSON_DATA,"r") as fd:
        ENGINEER_DATA = json.load(fd)  

def write_json():
    with open(JSON_DATA,"w") as fd:
        json.dump(ENGINEER_DATA,fd)

def get_argu(count):
    if len(sys.argv) >= count+2:
        return sys.argv[2:count+2]
    else:
        raise("Data not enough:")   

def find_indx(id):
    for indx in range(len(ENGINEER_DATA)):
        if ENGINEER_DATA[indx]["id"]==id:
            return indx
    return -1

def insert_data(id,name,age,gender):
    id = int(id)
    age = int(age)
    if find_indx(id) > -1:
        raise("data not existis")
    else:
        ENGINEER_DATA.append({
            "id":id,
            "name":name,
            "age":age,
            "gender":gender
        })
            
def update_data(id,key,val):
    id = int(id)
    indx = find_indx(id)
    if indx == -1:
        raise("Data not found")
    else:
        ENGINEER_DATA[indx][key] = val

def show_data(id):
    id = int(id)
    indx = find_indx(id)
    if indx == -1:
        raise("Data not found")   
    else:
        print(ENGINEER_DATA[indx])            

def delete_data(id):
    id = int(id)
    indx = find_indx(id)
    if indx == -1:
        raise("Data not found")
    else:
        ENGINEER_DATA.pop(indx)  


PROGRAM = sys.argv[0]     
CMD = None
try:
    CMD = sys.argv[1]
except:
    CMD ="--help"
    if CMD =="--help" or CMD == "--h":
        help_message()

try:
    if CMD =="insert":
        [id,name,age,gender] = get_argu(4)
        read_json()
        insert_data(id,name,age,gender)
        write_json()

    if CMD == "update":
        [id,field,new_value] = get_argu(3)
        read_json()
        update_data(id,field,new_value)
        write_json()
        
    if CMD == "show":
        [id] = get_argu(1)
        read_json() 
        show_data(id)  

    if CMD == "delete":
        [id] = get_argu(1)
        read_json()
        delete_data(id)
        write_json()

except Exception as e:
    print(e)        



