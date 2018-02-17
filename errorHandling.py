def divide(x, y):
     try:
         result = x / y
         print(result)
     except ZeroDivisionError:
         print("division by zero!")
     except ValueError:
         print("ValueError!!!!!!!!!!")
     else:
         print("result is", result)
     finally:
         print("executing finally clause")

x = int(raw_input("X/Y: X="))
y = int(raw_input("X/Y: Y="))
print('x/y', x,y)
if(x%y != 0):
    raise Exception ('Not divisible')
divide(x,y)
