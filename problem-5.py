# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam

s = input('enter any string:')
flag = True

for i in range(len(s)//2):
    if s[i] != s[len(s)- i -1 ]:
        flag = False 
        break
if flag:
    print("palandrome")
else:
    print('not a palandrome')



