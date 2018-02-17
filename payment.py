class Payment:
 def __init__ (self, fName,lName, rate, time, extra):
  self.fName = fName
  self.lName = lName
  self.rate = rate
  self.extra = extra
  self.time = time
  #print('You call init!')

      #print('Finish setting attribute!')
 def getName(self):
     return self.fName+' '+self.lName
 def getRate(self):
     return self.rate
 def getTime(self):
     return self.time
 def getExtra(self):
     return self.time
 def getPayment(self):
     paymentSum = self.time * self.rate + self.extra
     return paymentSum

#print('----------------------------------')
#ob = Payment()
