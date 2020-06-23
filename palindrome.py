mystring=input("Enter the string: ")
palin=0
# length=len(mystring)
# for i in range(length):
#     print(mystring[i])
#     if(mystring[i]!=mystring[length-(i+1)]):
#         palin=1
#         break
# if(palin==0):
#  print("string is palindrome")
# else:
#  print("string isn't palindrome)

if(mystring==mystring[::-1]):
    print("string is palindrome")
else:
    print("string isn't palindrome")
