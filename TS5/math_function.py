loop = 0

def input_number_1():
    n1 = float(input("Enter first number: "))
    return n1
    
def input_number_2():
    n2 = float(input("Enter second number: "))
    return n2

def divide():
    n2_check = 0
    while n2_check != 1:
        n1 = input_number_1()
        n2 = input_number_2()
        n2_check = num_2_check(n2)
    sum = n1 / n2
    print("Result: ", str(sum))

def num_2_check(n2):
    if n2 == 0:
        print("Error: the second number or denominator must not be equal to zero.")
        print("")
        return 0
    else:
        return 1

def exponentiation():
    n1 = input_number_1()
    n2 = input_number_2()
    sum = n1 ** n2
    print("Result: ", str(sum))
    
def remainder():
    n2_check = 0
    while n2_check != 1:
        n1 = input_number_1()
        n2 = input_number_2()
        n2_check = num_2_check(n2)
    sum = n1 % n2
    print("Result: ", str(sum))
    
def summation():
    n1 = input_number_1()
    n2 = input_number_2()
    sum = increment(n1, n2)
    print("Result: ", str(sum))
    
def increment(n1, n2):
    check = n1
    start = n1
    inc = n1
    end = n2 
    while check != end:
        inc += 1
        new_sum = start + inc
        check += 1
        start = new_sum 
    return start  

while loop != 1:
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("5 - Exit")
    print("")
    choice = input("Enter your choice: ")   
    if choice == "D" or choice == "d":
        divide()
        print("")
        
    elif choice == "E" or choice == "e":
        exponentiation()
        print("")
        
    elif choice == "R" or choice == "r":
        remainder()
        print("")
        
    elif choice == "F" or choice == "f":
        summation()
        print("")
        
    if choice == "5":
        loop = 1
        print("Exiting...")
        print("")    







