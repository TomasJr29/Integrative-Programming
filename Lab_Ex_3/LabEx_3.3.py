print(" ")

f_name = str(input("Enter your first name: "))
l_name = str(input("Enter your last name: "))
age = int(input("Enter your age: "))
contact_number = int(input("Enter your contact number: "))
course = str(input("Enter your course: "))

print(" ")

data = "Last Name: {}\nFirst Name: {}\nAge: {}\nContact Number: {}\nCourse: {}\n"

f = open("students.txt", "a")
f.write(data.format(l_name[0].upper() + l_name[1:].lower(), f_name[0].upper() + f_name[1:].lower(), age, contact_number, course.upper()))
f.close()

print("Student information has successfully been saved to 'students.txt'.")

print(" ")