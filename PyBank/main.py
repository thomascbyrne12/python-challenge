import os
import csv

#Declares Variables
great_change = 0
least_change = 0
count = 0
sum_change = 0
total = 0
first = False

#Locates csv file to read
filepath="C:\\Users\\Thomas Byrne\\Documents\\GitHub\\python-challenge\\PyBank"
csvpath = os.path.join(filepath, "budget_data.csv")

#Reads values from file
with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:

        #Skips header row
        if row[0] == 'Date':
            continue
        elif first == True:
            #Records change from last Profit/Loss
            change = int(row[1]) - last
            sum_change = sum_change + change
            #Records Greatest and Lowest Change values
            if change > great_change:
                great_change = change
                great_time = row[0]
            elif change < least_change:
                least_change = change
                least_time = row[0]

        #Sums total
        total = total + int(row[1])

        #Counts each month
        count = count + 1

        #Records value for future use
        last = int(row[1])
        first = True

#Calculating Average Change
avg_change = sum_change / count

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count}")
print("Average Change: ${:+.2f}".format(avg_change))
print("Greatest Increase in Profit/Loss: {} (${:.2f})".format(great_time, great_change))
print("Greatest Decrease in Profit/Loss: {} (${:+.2f})".format(least_time, least_change))
print("\n")

output_path = os.path.join(filepath, "myfile.txt")

with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {count}\n")
    txtfile.write("Average Change: {:.2f}\n".format(avg_change))
    txtfile.write("Greatest Increase in Profit/Loss: {} ({:+.2f})\n".format(great_time, great_change))
    txtfile.write("Greatest Decrease in Profit/Loss: {} ({:+.2f})\n".format(least_time, least_change))
