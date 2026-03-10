# Unoptimized Python code to find duplicate elements in a list

numbers = [5, 3, 8, 5, 2, 3, 9, 1, 8]

duplicates = []

for i in range(len(numbers)):
    count = 0
    
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count = count + 1
    
    if count > 1:
        already_present = False
        
        for k in range(len(duplicates)):
            if duplicates[k] == numbers[i]:
                already_present = True
        
        if already_present == False:
            duplicates.append(numbers[i])

print("Duplicate elements are:")
for i in range(len(duplicates)):
    print(duplicates[i])
