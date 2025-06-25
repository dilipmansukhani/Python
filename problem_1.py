"""54321
   4321
   321
   21
   1

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
"""

string = "ababa"
dictt = {}
ele = ""
for i in range(0,len(string)):
    for j in range(0,len(string)):
        ele=string[i:j+1]
        if ele in dictt:
            dictt[ele]+=1
        else:
            dictt[ele]=1
print(dictt)






                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
