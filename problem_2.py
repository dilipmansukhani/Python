# Arrange string chracter lowercase should come first

a = "ABCuyeTHGo"
lowercase = ""
upercase = ""

for chr in a:
    if chr.islower():
        lowercase+=chr
    else:
        upercase+=chr

result = lowercase + upercase
print(result)
