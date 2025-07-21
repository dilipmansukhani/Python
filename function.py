"""
# function define
def greeting():
    print("hello")
# function call
greeting()

# parameter <= username
def greeting(username):
    print("hello",username)
greeting("Naina")
greeting("Tushar")  # <= argument

y = 10 # global variable
def greeting(x):
    print(x+10,y)
greeting(20)
print("y:",y)

y = 10 # global variable
def greeting():
    global y
    y = 45
    print(y)
    
greeting()
print("y:",y)


def add(x,y):
    print(x+y)
a = 100
b = 200
add(12,b)


def add(a,b):
    print(a,b)
    a = 200
    b= 400
    
a=100
b = 400 
add(id(a),id(b))   


def add(list1): # list1 = mylist
    print("list func", list1)

    list1.append("hello")
    print("updated list",list1)

mylist = [10,20]
add(mylist)
print("mylist value", mylist)


mylist=[10,20]
lis1 = mylist
print(id(lis1),id(mylist))


def add(a):
    print("inside func",a)
  
    
a=100

add(a)   
print("outside",a)
print(id(a))

a=10
b=a

print(id(a),id(b))
a=12
print(id(a),id(b))
"""

def prime():
    n = 15
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
prime()