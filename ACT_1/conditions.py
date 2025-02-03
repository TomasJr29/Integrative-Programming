print()
print("Enter 3 Numbers")

inp1 = input("1st Number: ")
inp2 = input("2nd Number: ")
inp3 = input("3rd Number: ")

new_inp1 = int(inp1)
new_inp2 = int(inp2)
new_inp3 = int(inp3)

highest = 0

if new_inp1 > new_inp2:
    highest = new_inp1
    if highest < new_inp3:
        highest = new_inp3
        print("The highest number is: " + str(highest))
    else:
        print("The highest number is: " + str(highest))
else :
    highest = new_inp2
    if highest < new_inp3:
        highest = new_inp3
        print("The highest number is: " + str(highest))
    else: 
        print("The highest number is: " + str(highest))



    
    




