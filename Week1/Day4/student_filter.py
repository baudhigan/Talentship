import csv 

try:
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)

        with open("passed_students.csv", "w", newline="") as output:
            writer = csv.DictWriter(
                output,
                fieldnames=["name", "marks"]
            )
            writer.writeheader()

            for row in reader:
                marks = int(row["marks"])

                if marks >= 60:
                    writer.writerow(row)
    print("Filtered Data Saved Successfully!")

except FileNotFoundError:
    print("File is  Missing.")
except KeyError:
    print("Required column is missing.")
except ValueError:
    print("Invalid Marks value.")
except Exception as e:
    print("Unexpected Error.")

finally:
    print("Program is run Successfully!")