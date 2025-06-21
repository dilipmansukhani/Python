"""
*
**
*  *
*   *
*  *
* *
*

"""
for i in range(1,5):
    for j in range(1,i+1):
        if(j==1 or i==j):
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,4):
    for j in range(i,4):
        if(j==1 or j==4-i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
