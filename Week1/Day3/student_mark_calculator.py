#Student Mark Calculator using Dictionary

students = {
    "Ram": 93,
    "Nithin": 85,
    "Kamal": 86,
    "Arya": 98,
    "Surya": 77
}


for names, marks in students.items():
    print(names, ":", marks)

total = 0

for marks in students.values():
    total = total + marks

average = total / len(students)

print("Total Marks:", total)
print("Average Marks:", average)