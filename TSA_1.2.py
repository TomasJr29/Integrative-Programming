inp = input("Please enter a String: ")

new_inp = inp.replace(" ", "")

only_others = ""

only_numbers = ""

total_sum = 0

for i in new_inp: 
    
    if (i.isdigit()):
        only_numbers += i
        
    else:
        only_others = i.replace(i, "")
        
for i in only_numbers:
    
    total_sum += int(i)
    
print("Sum of the digits in the string: " + str(total_sum))
