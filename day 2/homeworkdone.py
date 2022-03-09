#name=giorgi
#surname=aptsiauri
#grade=90

name = input("enter your name: ")
surname = input("enter your surname: ")
grade = input("enter your grade: ")

print(name.count("i"))
print(surname[3:9] is "shvili")
if int(grade) > 50:
    print("you win", name, surname, grade)
else:
    print("you lose", name, surname, grade)