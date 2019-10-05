import os
import csv

#Declares Variables
count = 0
candidates = []
votes = []
percentage = []
most = 0
large = 0

#Locates csv file to read
filepath="C:\\Users\\Thomas Byrne\\Documents\\GitHub\\python-challenge\\PyPoll"
csvpath = os.path.join(filepath, "election_data.csv")

#Reads values from file
with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:

        if row[0] == 'Voter ID':
            continue
        elif row[2] not in candidates:
            candidates.append(row[2])
            votes.append(1)
        elif row[2] in candidates:
            index = candidates.index(row[2])
            votes[index] = votes[index] + 1

        count = count + 1

    for num in votes:
        if num > large:
            large = num
            winner = candidates[votes.index(num)]

percentage.append(votes[0]/count)
percentage.append(votes[1]/count)
percentage.append(votes[2]/count)
percentage.append(votes[3]/count)

ki = candidates.index('Khan')
ci = candidates.index('Correy')
ti = candidates.index("O'Tooley")
li = candidates.index('Li')

print("Election Results")
print("----------------------------")
print(f"Total Votes: {count}")
print("----------------------------")
print("Khan: {:.2%} ({})".format(percentage[ki], votes[ki]))
print("O\'Tooley: {:.2%} ({})".format(percentage[ti], votes[ti]))
print("Coorey: {:.2%} ({})".format(percentage[ci], votes[ci]))
print("Li: {:.2%} ({})".format(percentage[li], votes[li]))
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

output_path = os.path.join(filepath, "myfile.txt")

with open(output_path, 'w') as txtfile:

    txtfile.write("Election Results\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Votes: {count}\n")
    txtfile.write("----------------------------\n")
    txtfile.write("Khan: {} ({})\n".format(percentage[ki], votes[ki]))
    txtfile.write("O\'Tooley: {} ({})\n".format(percentage[ti], votes[ti]))
    txtfile.write("Coorey: {} ({})\n".format(percentage[ci], votes[ci]))
    txtfile.write("Li: {} ({})\n".format(percentage[li], votes[li]))
    txtfile.write("----------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("----------------------------\n")
