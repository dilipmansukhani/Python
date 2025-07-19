# Write a program which can remove a particular character from a string.

s = input('enter any string')
term = input('anything you want to remove?')

result = ""

for i in s:
    if i != term:  # not in isliye use kiya jo term m likhege vo hatana h(usko chor kr ajayega baki ka)
                        # == krte toh jo hatana h wahi ajata 
        result+=i      #result = result + i 
print("modified string:", result)