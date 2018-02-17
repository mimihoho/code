def isOdd(num):
    return num%2 == 1

def isEven(num):
    return num%2 == 0

def divisibleBy(num, n):
    return num%n == 0

def checkArray(numbers):
    for num in numbers:
        if isEven(num):
            if divisibleBy(num,3):
                print("eventhree")
            else:
                print(num)
        elif isOdd(num):
            if divisibleBy(num,3):
                print("three")
            else:
                print("odd")

checkArray([])
checkArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
checkArray([1,2,6,7,9,4,10,11,12,3,13,24])
