import unicodecsv
import numpy as np


titanic_filename = "C:/Users/Administrator/Desktop/titago/AWS/titanic/titanic-data.csv"

def open_csv(file):
    with open(file, 'rb') as f:
        reader = unicodecsv.DictReader(f,encoding='utf-8')
        return list(reader)

def parse_maybe_int(i):
    if i== '':
        return None
    else:
        return int(float(i))

def parse_maybe_float(i):
    if i== '':
        return None
    else:
        return float(i)

def get_unique_Passenger(data):
    unique_Passenger = set()
    for data_point in data:
        unique_Passenger.add(data_point['Name'])
    return unique_Passenger

titanic_data = open_csv(titanic_filename)

for data in titanic_data:
    data['Age'] = parse_maybe_int(data['Age'])
    data['Survived'] = data['Survived'] == '1'
    data['Pclass'] = parse_maybe_int(data['Pclass'])
    data['SibSp'] = parse_maybe_int(data['SibSp'])
    data['Parch'] = parse_maybe_int(data['Parch'])
    data['Fare'] = parse_maybe_float(data['Fare'])




print titanic_data[1]
print len(titanic_data)
print len(get_unique_Passenger(titanic_data))
