inp = input("Please enter a String: ")

space_num = 0
vowel_num = 0
consonant_num = 0
special_num = 0
number_num = 0

if " " in inp:
    space_num = int(inp.count(" "))
    
new_inp = inp.replace(" ", "")

for i in new_inp:
    if (i in ('A', 'a', 'e', 'E', 'i', 'I', 'o', '0' , 'u' , 'U')):
        vowel_num += 1
        
    if (i in ('B', 'b', 'C', 'c', 'D', 'd', 'F', 'f', 'G', 'g', 'H', 'h', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z')):
        consonant_num += 1
        
    if(i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
        number_num += 1
        
    if (i not in ('0', '1', '2', '3','4','5','6','7','8','9','A', 'a', 'e', 'E', 'i', 'I', 'o', '0' , 'u' , 'U','B', 'b', 'C', 'c', 'D', 'd', 'F', 'f', 'G', 'g', 'H', 'h', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z')):
        special_num += 1

print("Number of spaces in the string: ", space_num)

print("Number of vowels in the string: ", vowel_num)

print("Number of consonants in the string: ", consonant_num)

print("Number of numbers in the string: ", number_num)

print("Number of special characters in the string: ", special_num)


