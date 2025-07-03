
list = [1, 2, 3, 5, 6, 8, 7]
newlist = []
for i in range(0,len(list)):
    if(list[i]%2!=0):
        newlist.append(list[i])  # for nested list newlist.append([list[i]])
print(newlist)
