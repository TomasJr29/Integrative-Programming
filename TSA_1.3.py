
#  a. use nested for statement 

print(" ")
print(" a. use nested for statement  ")
print(" ")

a_display = ""

spces = " "

for i in range(1, 6):
    
    for j in range(5, i, -1):
        print(spces, end = "")

    a_display += str(i)
    print(a_display)
    
#----------------------------------------------------------

print(" ")
print("=================================================")
print(" ")

#  b. use nested while statement

print("b. use nested while statement  ")
print(" ")

b = 1

k = 1

p = 1

while b < 8:
    
    while k <= b:
        
        if b % 2 == 0 and b != 6:
            break  
        
        else:
            print(b, end = "")  
            
        k += 1

    if b % 2 == 0 and b != 6:
        p += 1
        
    elif b % 2 != 0 or b == 6:  
        print(" ")  

    b += 1
    
    k = 1

print(" ")
print(" ")  


    
