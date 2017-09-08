import pandas as pd
import pandasql
import unicodecsv


subway_filename = "C:/Users/Administrator/Desktop/titago/AWS/titanic/weather-underground.csv"
turnstile_filename = "C:/Users/Administrator/Desktop/titago/AWS/titanic/turnstile-110528.txt"

def open_csv(file):
    with open(file, 'rb') as f:
        reader = unicodecsv.DictReader(f,encoding='utf-8')
        return list(reader)

def num_rainy_days(filename):
    weather_data = pd.read_csv(filename)

    q = "select min(mintempi) from weather_data where rain = 1 and mintempi > 55 ;"
    rainy_days = pandasql.sqldf(q,locals())
    return rainy_days

def fix_turnstile_data(filename):
    turnstile_df = open_csv(filename)

    return turnstile_df


# print num_rainy_days(subway_filename)

print fix_turnstile_data(turnstile_filename)