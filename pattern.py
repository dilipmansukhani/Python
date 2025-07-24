"""
for i in range(1,5):
    for s in range(1,i):
        print(" ",end='')
    for j in range(1,5):
        print("*",end="")
    print()


for i in range(1,6):
    for j in range(1,6):
        if i==1 or j==1 or i==5 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


for i in range(1,6):
    a = "Af"
    for j in range(1,i+1):
        print(a,end="")
        a = chr(ord(a)+1)
    print()


a = "A"
for i in range(1,6):
    for j in range(1,i+1):
        print(a,end="")
    a = chr(ord(a)+1)
   
    print()


a = "E"
for i in range(1,6):
    for j in range(ord(a)+1-i,70):
        print(chr(j),end="")

    print()

for i in range(1,6):
    for s in range(i,5):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


for i in range(1,6):
    a = 1
    for s in range(i,5):
        print(" ",end="")
    for j in range(1,i+1):
        print(a,end="")
        a+=1
    print()


for i in range(1,6):
    a = 1
    for s in range(1,i):
        print(" ",end="")
    for j in range(i,6):
        print(a,end="")
        a+=1
    print()


for i in range(1,6):
    a = "A"
    for s in range(1,i):
        print(" ",end="")
    for j in range(i,6):
        print(a,end="")
        a = chr(ord(a)+1)
    print()


for i in range(1,6):
    for s in range(i,5):
        print(" ",end='')
    for j in range(1,6):
        print("*",end="")
    print()


for i in range(1,6):
    a=1
    for s in range(i,5):
        print(" ",end='')
    for j in range(1,6):
        print(a,end="")
        a+=1
    print()


for i in range(1,6):
    a="A"
    for s in range(i,5):
        print(" ",end='')
    for j in range(1,6):
        print(a,end="")
        a= chr(ord(a)+1)
    print()


for i in range(1,5):
    for s in range(i,4):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


for i in range(1,5):
    for s in range(i,4):
        print(" ",end="")
    for j in range(1,i+1):
        if j==1 or j==i or i==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


for i in range(1,5):
    for s in range(1,i):
        print(" ",end="")
    for j in range(8-2*i+1):
        print("*",end="")
    print()

for i in range(1,5):
    for s in range(1,i):
        print(" ",end="")
    for j in range(2*i-1,8):
        if i==1 or j==7 or j==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()


for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(1,4):
    for j in range(i,4):
        print("*",end="")
    print()


for i in range(1,5):
    for s in range(i,4):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(1,4):
    for s in range(1,i+1):
        print(" ",end="")
    for j in range(i,4):
        print("*",end="")
    print()


for i in range(1,5):
    for s in range(i,4):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
for i in range(1,4):
    for s in range(1,i+1):
        print(" ",end="")
    for j in range(2*(i+1)-1,8):
        print("*",end="")
    print()


for i in range(1,6):
    a = 1
    for j in range(1,i+1):
        print(a,end="")
        a+=1
    print()


for i in range(1,6):
    a=1
    for j in range(i,6):
        print(a,end="")
        a+=1
    print()


for i in range(1,6):
    a = 1
    for j in range(1,i+1):
        if j==1 or j==i or i==5:
            print(a,end=" ")
            
        else:
            print(" ",end=" ")
        a+=1
    print()


for i in range(1,6):
    
    for s in range(i,6):
        print(" ",end="")
    for j in range(i,2*i):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
       
    print()


for i in range(1,6):
    a=1
    for s in range(i,5):
        print(" ",end="")
    for j in range(1,i+1):
        if j==1 or j==i or i==5:
            print(a,end=" ")
        else:
            print(" ",end=" ")
        a+=1
    print()


a=1
for i in range(1,6):
    
    for j in range(i,6):
        if j==1 or j==6-i or i==1:
            print(a,end=" ")
    
        else:
            print(" ",end=" ")
        
    
        
    print()

a = "A"
for i in range(1,6):
    for j in range(1,i+1):
        print(a,end="")
        a = chr(ord(a)+1)
   
    print()

1 2 3 4 5
2     5
3   5
4 5
5



    
a=1
for i in range(1,6):
    
    for j in range(1,6):
        if j==1 or j==6-i or i==1:
            print(a,end=" ")
    
        else:
            print(" ",end=" ")
        if j == 1 or j == 6 - i or i == 1:  # Increment only when printing a number
            a += 1
    print()


a = 1
for i in range(1, 6):  # Loop for rows
    for j in range(1, 6):  # Loop for columns
        if j == 1 or j == 6 - i or i == 1:  # Print numbers for the first row, first column, or diagonal
            print(a, end=" ")
        else:  # Print spaces otherwise
            print(" ", end=" ")
        if j == 1 or j == 6 - i or i == 1:  # Increment only when printing a number
            a += 1
    print()  # Move to the next line after each row


for i in range(1,6):
    
    
    for j in range(i,6):
        if j==i or j==5 or i==1:
            print(j,end=" ")
        else:
            print(" ",end=" ")
        
        
        
        
    print()
"""
"""
1
22
333
4444
55555
"""

num = int(input("Enter Number"))

for i in range(1,num):
    for j in range(1,i+1):
        print(i,end="")
    print()
