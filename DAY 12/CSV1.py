import csv
import os
#csv_file_path='Salary_Data.csv'
csv_file_path='c:\\Users\\Aparna\\Desktop\\Hexaware Python\\CSVDemo\\salary_data.csv'
with open(csv_file_path,'r') as file:
    csv_reader=csv.reader(file)
    for row in csv_reader:
        print(row) 
csv_file_path = os.path.abspath('salary_data.csv')
with open(csv_file_path) as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
print(header)
print(rows)
