# Create a method that returns the five most frequent lottery number in a pretty table format
from prettytable import PrettyTable
import csv
from collections import Counter
def five_most_frequent():
    f = open('C:/Users/Gáspár/Desktop/Greenfox/szuri92/week-04/day-1/lottery/otos.csv')
    csv_f = csv.reader(f, delimiter=";")
    all_num = []
    for row in csv_f:
        i = 1
        while i <= 5:
            all_num.append(row[len(row)-i])
            i += 1
    count = Counter(all_num)
    #print(count)

    most_common = count.most_common()
    #print(most_common)
    top_five = []
    i = 0
    while i < 5:
        top_five.append(most_common[i])
        i += 1


    table = PrettyTable(["number", "frequency"])
    for i in range(len(top_five)):
        table.add_row(top_five[i])

    return table


print(five_most_frequent())
