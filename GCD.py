num1 = int(input('Enter number: '))
num2 = int(input('Enter 2nd number: '))

if num1 > num2:
    smallerN = num2
    biggerN = num1
else:
    smallerN = num1
    biggerN = num2

CommonFactor = list()

for i in range(1, smallerN):
    if((smallerN % i == 0) and (biggerN % i ==0)):
        print('Warikireru number: ', i)
        greatest = i
        if greatest <= i:
            greatest = i
print('Greatest common D is ', greatest)
