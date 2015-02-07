import os
import re
import sys
import pymongo


# Looks for local baby names directory and outputs a dictionary in the format year: "name,sex,num_occurrence".
def get_data():
    data = {}
    names = os.getcwd() + '/names'
    if os.path.exists(names):
        names_dir = os.listdir(names)
        for yob in names_dir:
            if yob[-4:] == '.txt':
                year = re.search(r'\d\d\d\d', yob)
                with open(names + '/' + yob) as txt:
                    data[year.group()] = re.findall(r'\S+', txt.read())
        return data
    return "names directory not found!"


# Cleans up data for friendly JSON output
def fix_data(data):
    fixed_data = {}
    temp = {}
    for year in data:
        id = 0
        for value in data[year]:
            name = re.search(r'\w+', value).group()
            sex = re.search(r'(,)(\w+)', value).group()[1]
            num_occurrence = re.search(r'\d+', value).group()
            temp[id] = {"name": name, "sex": sex, "num_occurrence": num_occurrence}
            id += 1
        fixed_data[year] = temp.values()
    return fixed_data


# Outputs fixed_data to MongoDB
def sendto_mongo(fixed_data):
    connection = pymongo.Connection("mongodb://localhost", safe=True)
    db = connection.social_security_data
    baby_names = db.baby_names
    for year in fixed_data:
        try:
            baby_names.insert({"_id": year, "info": fixed_data[year]})
        except:
            print "Unexpected error:", sys.exc_info()[0]



