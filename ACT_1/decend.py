print()
print("Enter 3 Numbers")

inp1 = input("1st Number: ")
inp2 = input("2nd Number: ")
inp3 = input("3rd Number: ")

new_inp1 = int(inp1)
new_inp2 = int(inp2)
new_inp3 = int(inp3)

highest = 0
mid = 0
lowest = 0

print("----------------------------------")

if new_inp1 > new_inp2:
    highest = new_inp1
    if highest < new_inp3:
        highest = new_inp3
        mid = new_inp1
        lowest = new_inp2
        print("Highest: " + str(highest))
        print("Middle: " + str(mid))
        print("Lowest: " + str(lowest))
    else:
        print("Highest: " + str(highest))
        if new_inp2 < new_inp3:
            mid = new_inp3
            lowest = new_inp2
            print("Middle: " + str(mid))
            print("Lowest: " + str(lowest))
        else:
            mid = new_inp2
            lowest = new_inp3
            print("Middle: " + str(mid))
            print("Lowest: " + str(lowest))
else :
    highest = new_inp2
    if highest < new_inp3:
        highest = new_inp3
        mid = new_inp2
        lowest = new_inp1
        print("Highest: " + str(highest))
        print("Middle: " + str(mid))
        print("Lowest: " + str(lowest))
    else: 
        print("The highest number is: " + str(highest))
        if new_inp1 < new_inp3:
            mid = new_inp3
            lowest = new_inp1
            print("Middle: " + str(mid))
            print("Lowest: " + str(lowest))
        else:
            mid = new_inp2
            lowest = new_inp1
            print("Middle: " + str(mid))
            print("Lowest: " + str(lowest))