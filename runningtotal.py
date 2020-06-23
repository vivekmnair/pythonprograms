array1=[]
n=int(input("Enter the number of elements in list: "))
sum=0
for i in range(1,n+1):
    number=int(input("enter element"))
    sum+=number
    array1.append(int(number))
print("total is",sum)
