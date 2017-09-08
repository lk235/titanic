import pandas as pd
import pandasql
import json
import requests
import numpy as np


baseball_filename = "C:/Users/Administrator/Desktop/titago/AWS/baseballdatabank-2017.1/core/Master.csv"
new_filename = "C:/Users/Administrator/Desktop/titago/AWS/baseballdatabank-2017.1/core/Master_new.csv"
aadhaar_filename = "C:/Users/Administrator/Desktop/titago/AWS/titanic/aadhaar_data.csv"
result_filename = "C:/Users/Administrator/Desktop/titago/9.7/new/result.xlsx"

def add_full_name(path_to_csv, path_to_new_csv):
    df = pd.read_csv(path_to_csv)
    df['nameFull'] = df['nameFirst'] + " " + df ['nameLast']

    new_csv = df.to_csv(path_or_buf=path_to_new_csv)
    return new_csv

def select_first_50(filename):
    aadhaar_data = pd.read_csv(filename)
    aadhaar_data.rename(columns=lambda x: x.replace(' ', '_').lower(), inplace=True)
    q = "select * from aadhaar_data limit 50;"
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution

# add_full_name(baseball_filename,new_filename)

# print (select_first_50(baseball_filename))

baseball_df = pd.read_csv(baseball_filename)


mean_weight = np.mean(baseball_df['weight'])
baseball_df['weight'] = baseball_df['weight'].fillna(mean_weight)
print baseball_df.describe()

result_df = pd.read_excel(result_filename)
print result_df.describe()