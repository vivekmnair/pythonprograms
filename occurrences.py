mystring=input("enter string:")
character=input("enter character:")
count=0
for i in mystring:
    if i == character: 
        count = count + 1
ext= ("Count of %s is %d times:" %(character,count))
print(ext)    
  