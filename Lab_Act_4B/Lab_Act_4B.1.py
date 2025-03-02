set_A = {"a", "b", "c", "d", "f", "g"}
set_B = {"b", "c", "h", "l", "m", "o"}
set_C = {"c", "d", "f", "h", "i", "j", "k"}

tup_set_AB = tuple(set_A) + tuple(set_B)

set_AB = set(tup_set_AB)

print("")

print("Total number of elements are there in set A and B are " + str(len(set_AB)))

print("")

tup_set_b = tuple(set_B)

tup_set_c = tuple(set_C)

tup_set_AC = tuple(set_A) + tuple(set_C)

set_AC = set(tup_set_AC)

new_tup_set_AC = tuple(set_AC)

new_tup = tuple()

count = 0

for i in new_tup_set_AC:
    for j in tup_set_b:
        if j == i:
            count += 1
            
print("Total number of elements are there in set A and C are " + str(count))

print("")

print("i  : ", set_C.difference(set_A))

print("ii : ", set_C.intersection(set_A))

print("iii: ", set_B.intersection(set_A.union(set_C)))

print("iv : ", set_A.intersection(set_C.difference(set_B)))

print("v  : ", set_A.intersection(set_C.intersection(set_B)))

print("v  : ", set_B.difference(set_C.union(set_A)))
        
print("")



