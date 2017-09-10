import pandas as pd
import pandasql
import unicodecsv
import csv


subway_filename = "C:/Users/Administrator/Desktop/titago/AWS/titanic/weather-underground.csv"
# turnstile_filename = "C:/Users/Administrator/Desktop/titago/AWS/titanic/turnstile-110528.txt"
turnstile_filename = "C:/Users/lk235/Desktop/titago/titanic/turnstile-110528.txt"
solution_turnstile_filename = "C:/Users/lk235/Desktop/titago/titanic/solution_turnstile-110528.txt"
file1 = "C:/Users/lk235/Desktop/titago/7.2/new tables/FORMA_ITALIA.csv"
file2 = "C:/Users/lk235/Desktop/titago/7.2/new tables/ingromaket07.csv"
file_xlsx = "C:/Users/lk235/Desktop/titago/7.2/new tables/FORMA_ITALIA.xlsx"

out_put = "C:/Users/lk235/Desktop/titago/7.2/new tables/output.csv"


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
    f_in = open(filename,'r')
    f_out = open(solution_turnstile_filename, 'w')
    reader_in = csv.reader(f_in,delimiter = ',')
    writer_out = csv.writer(f_out, delimiter = ',')
    # reader_in.next()
    for line in reader_in:

        line_start = [line[0],line[1],line[2]]

        step = 5
        i = 3
        while i < len(line):
            new_line = line_start + line[i:i + step]
            i = i + step
            writer_out.writerow(new_line)



    f_in.close()
    f_out.close()

def create_master_turnstile_file(filenames, output_file):
    with open(output_file, 'w') as master_file:
        master_file.write('EAN,Descrizione,Ivato\n')
        for filename in filenames:
            f_in = open(filename, 'r')

            reader_in = csv.reader(f_in, delimiter=',')
            reader_in.next()
            writer_out = csv.writer(master_file, delimiter=',')
            for line in reader_in:
                new_line = [line[0],line[1],line[3]]

                writer_out.writerow(new_line)


create_master_turnstile_file([file1,file2],out_put)

def filter_by_regular(filename,col_name,col_value):
    file_df = pd.read_csv(filename)
    return file_df[file_df[col_name] == col_value]

def filter_by_value_xlsx(filename,col_name,col_value):
    file_df = pd.read_excel(filename)
    return file_df[file_df[col_name] == col_value]

print filter_by_value_xlsx(file_xlsx,'Barcode','8000162003064')




# print num_rainy_days(subway_filename)

# fix_turnstile_data(turnstile_filename)