class AgeError(Exception):
    pass

age=20

try:
    if age < 18:
        raise AgeError("Must be above 18")
    else:
        print("Accepted")

except AgeError as e:
    print(e)
