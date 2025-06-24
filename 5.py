l = [10,15,2]
gratest  = 0
second_gratest = 0
for i in range(0,len(l)):
    if l[i]>gratest:
        second_gratest = gratest
        gratest = l[i]
    elif l[i] > second_gratest:
        second_gratest = l[i]
print(second_gratest)