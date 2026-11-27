# file = open("sample.txt", "r")
# content = file.read()
# print(content)
# file.close()


# #using with 

# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)


#reading csv files
    
import csv

with open("students.csv", "r") as file:
    content = csv.DictReader(file)

    for row in content:
        if int(row["marks"])>=60:
            print(row["name"], row["marks"])