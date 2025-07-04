# Take a list and find out the second  highest number
mylist= [10,201,401,210,400, 3,4,5,8]
"""
grater = 0
second_grater = 0

for i in mylist:
    if i > grater:
        second_grater = grater
        grater = i
    elif i > second_grater and i!=grater:
        second_grater = i
print(second_grater)
"""
for i in range(0,2):
    for j in range(i+1,len(mylist)):
        if(mylist[j]>mylist[i]):
            temp = mylist[i]
            mylist[i] = mylist[j]
            mylist[j]=temp

print(mylist[0], mylist[1])