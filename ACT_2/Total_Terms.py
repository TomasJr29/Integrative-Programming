inp1 = int(input("1st Number: "))
inp2 = int(input("2nd Number: "))

count = 0
end = 0

if inp1 < inp2:
    count = inp1 
    end = inp2 + 1 
    
elif inp2 < inp1:
    count = inp2 
    end = inp1 + 1
    
elif inp1 == inp2:
    count = inp1 
    end = inp2 + 1

total_sum = 0

while  count != end:
    
    total_sum += count
    
    count += 1

print("The sum of the numbers are " + str(total_sum))