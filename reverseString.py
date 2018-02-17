string = "OMAEHA AHOKA!"
rString = string[::-1]
print(rString)

i = len(rString)
#count = 0
backToString = []

print("rString length", len(rString), i)

while (i > 0):
#for i in range(i, 0, -1):
    print('i',i)
    #print('count',count)
    #print('rString:', rString[i-1])
    backToString.append(rString[i-1])
    i = i-1
    #count = count+1
print(backToString)
print("Python3")
