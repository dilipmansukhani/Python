a=1
for i in range(1,6):
    
    for j in range(1,i+1):
        if j==1 or i==5 or j==i:
            print(a,end="")
            a+=1
        else:
            print(" ",end="")
        
    print()
