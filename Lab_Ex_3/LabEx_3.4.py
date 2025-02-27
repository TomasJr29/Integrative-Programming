print(" ")

print("Reading Stdent Information: \n")

f = open("students.txt", "r")
while True:
    try:
        with open("data.txt", "r") as file:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")
        break
f.close()
    



