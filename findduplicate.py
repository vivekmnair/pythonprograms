array1 = [1,2,5,6,7,2,4,1,7,5]
print("Duplicate elements in given array are: ") 
for i in range(0, len(array1)):    
    for j in range(i+1, len(array1)):    
        if(array1[i] == array1[j]):    
            print(array1[j])