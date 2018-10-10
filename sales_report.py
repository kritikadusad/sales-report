"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

# My code:
sales_report_data = {}
with open("sales-report.txt") as file:
    for line in file:
        line = line.rstrip()
        each_line = line.split("|")
        salesperson = each_line[0]
        melons_sold = int(each_line[2])
        if salesperson not in sales_report_data.keys():
            sales_report_data[salesperson] = melons_sold
        else:
            sales_report_data[salesperson] += melons_sold
salespeople = sales_report_data.keys()

for i in range(len(salespeople)):
    print("{} sold {} melons".format(salespeople[i], sales_report_data[salespeople[i]]))

# for i in range(len(sales_report_data.keys())):
#     print("{} sold {} melons".format(sales_report_data.keys(), sales_report_data.keys()[i]))

# # Solution code:
# # Made 2 empty lists that will have the names of the salespeople and the number of melons they have sold.
# salespeople = []
# melons_sold = []
# # Opening the txt file her.
# f = open("sales-report.txt")
# # a for loop going through the object f:
# for line in f:
#     # Stripping each line off of \n
#     line = line.rstrip()
#     # splitting each line by | and storing it into a list called entries.
#     entries = line.split("|")
#     # salesperson variable takes in first element from the list-entries
#     salesperson = entries[0]
#     # melon variable takes in third element from the list-entries
#     melons = int(entries[2])
#     # checking to see if the salesperson is in the list salespeople.
#     if salesperson in salespeople:
#         # position variable takes in index of the salesperson added.
#         position = salespeople.index(salesperson)
#         # At the same position as the salesperson, the number of melons are added.
#         melons_sold[position] += melons
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)

# for i in range(len(salespeople)):
#     print("{} sold {} melons".format(salespeople[i], melons_sold[i]))
