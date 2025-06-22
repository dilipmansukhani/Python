# print prime numbers 2 to 15:
def primenumber():
    for i in range(2,15):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
primenumber()

