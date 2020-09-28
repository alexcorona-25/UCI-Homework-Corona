import os
import csv

#Stating where our file is located (Saved on my desktop)
cvspath = os.path.join('Resources', 'budget_data.csv')

#Creating empty lists to store varibales throughout the data
total_months = []
total_profit = []
month_change =[]
with open(cvspath) as budget:
    csvreader=csv.reader(budget, delimiter=',')

    #Skip Header for Row Count
    csv_headr = next(csvreader)

    for row in csv.reader(budget):
    #Append the value found for months and profits to the new varibales list created
        total_months.append(row[0])  
        total_profit.append(int(row[1]))
    
    #create a loop that runs through profits to get the monthy to month change
    for i in range(len(total_profit)-1):

        #Finding the Value of the month to month change and appending to the list
        month_change.append(total_profit[i+1]-total_profit[i])
     
#Finding the greatest increase in profit
greatest_increase = max(month_change)

#Finding the greatest decrease
greatest_decrease = min(month_change)

# Correlate max and min to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month

max_increase_month = month_change.index(max(month_change)) + 1
max_decrease_month = month_change.index(min(month_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(month_change)/len(month_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(greatest_decrease))})")

#Creating where our summary will be saved
cvspath = os.path.join('Analysis', 'budget_data_code_summary.txt')
with open(cvspath,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(month_change)/len(month_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(greatest_decrease))})")