import re
import csv

with open("contacts.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)