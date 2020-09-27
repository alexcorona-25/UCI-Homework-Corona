import os
import csv

cvspath = os.path.join("..", "..", "..", budget_data)

with open(cvspath) as budget:
    csvreader=csv.reader(budget, delimiter=',')

    #Skip Header for Row Count
    csv_headr = next(csvreader)

    total = 0
    for row in csv.reader(budget):
        total += int(row[1])

   months = len(list(csvreader)

   print("Financial Analysis")
   print("------------------")
   print(f"Total Months ({months}")
   print(f"Total:$ {total}")