import unicodecsv
import numpy as np
import pandas as pd
from collections import defaultdict
import statsmodels.api as sm

titanic_filename = "C:/Users/Administrator/Desktop/titago/AWS/titanic/titanic-data.csv"

def open_csv(file):
    with open(file, 'rb') as f:
        reader = unicodecsv.DictReader(f,encoding='utf-8')
        return list(reader)

def parse_maybe_int(i):
    if i== '':
        return 0
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




# print titanic_data[1]
# print len(titanic_data)
# print len(get_unique_Passenger(titanic_data))

titanic_by_survived = defaultdict(list)
for data_point in titanic_data:
    is_survived_key = data_point['Survived']
    titanic_by_survived[is_survived_key].append(data_point)

total_age_by_survived = {}
for is_survived_key,ages in titanic_by_survived.items():
    total_age = 0
    for age in ages:

        total_age = total_age + age['Age']
    total_age_by_survived[is_survived_key] = total_age



total_age = total_age_by_survived.values()
# print titanic_by_survived[False]
# print titanic_by_survived[True]
# print titanic_by_survived
# print total_age
# print np.mean(total_age)
# print np.min(total_age)
# print np.max(total_age)
# print np.std(total_age)

predictions = {}
df = pd.read_csv(titanic_filename)

for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        # if passenger['Sex'] == 'male':
        #     predictions[passenger_id] = 0
        # else:
        #     predictions[passenger_id] = 1

        if passenger['Sex'] == 'female' or passenger['Age'] < 18 and passenger['Pclass'] ==1:
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0

print predictions