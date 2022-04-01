import csv

with open('Netflix subscription fee Dec-2021.csv','r') as csv_file:
    csv_reader = csv.reader(csv.file)

    for line in csv_reader:
        print(line)





