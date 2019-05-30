'''
Создайте список словарей:
        [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
Запишите содержимое списка словарей в файл в формате csv
'''


import csv

with open('csvfile.txt', 'r', encoding='utf-8') as f:
    fields = ['name', 'age', 'job']
    reader = csv.DictReader(f, fields, delimiter=',')
    for row in reader:
        print(row)