# write a programne that add two elements and give target value.

list = [6, 3, 4, 5,1 ,8]
target = 9

for i in range(0,len(list)):
    for j in range(1+i,len(list)):
        if list[i] + list[j] == target:
            print(list[i],list[j])