class MyClass1:
    count = 0
    def __init__(self):
        self._val1 = 0
        print("1")
        MyClass1.count += 1

    def setVal(self, num):
       self._val1 = num

    def getVal(self):
        return self._val1

class MyClass2(MyClass1):
    def __init__(self):
        print("2")
        #super(MyClass2, self).__init__() #For Pytohn2.7
        super().__init__()
        MyClass1.count += 1


a = MyClass2()
b = MyClass2()
a.setVal(123)
print(a._val1)               #=> 123
print("COUNT:", a.count)
#print(a.val2)              #=> 456
#print a.getVal()

"""with Super class, we can access variables in parent class"""
"""Otherwise, we need methods to set & get from child's class"""
