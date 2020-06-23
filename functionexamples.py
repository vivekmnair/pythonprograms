import random

print(random.random())

print(random.randrange(0,10))

print(random.uniform(0,10))

a=10
b=20

c=a
a=b
b=c

print(a)
print(b)

a=10
b=20

a,b=b,a

print(a)
print(b)

try:
    print(x)
except:
    print("an exception occurred")

try:
    print(x)
except Exception as e:
    print(e)

try:
    print(x) 
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")

try:
    x=10
    print(x/0)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")

try:
    x=10
    print(x/0)
except NameError:
    print("variable x is not defined")
except Exception as e:
    print(e)

x = -1
if(x<0):
    raise Exception("sorry no numbers below zero")

def divide(a,b):

    if(b==0):
        raise Exception("sorry cant divide these numbers")
    else:
        return a/b

try:
    print(divide(3,0))
except Exception as e:
    print(e)

try:
    print(divide(3,2))
except Exception as e:
    print(e)

def foo():
    try:
        return 1
    finally:
        return 2
print(foo())

    


