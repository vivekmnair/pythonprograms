array1=[]
n=int(input("Enter the number of elements in list: "))
for i in range(1,n+1):
    number=int(input("enter element"))
    array1.append(int(number))
array1.sort()
print("largest element is",array1[n-1])