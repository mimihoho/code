from pyClass import Payment
from datetime import date
import string

# Of if without using __init__.py, user
#From .pyClass import Payment

choice = raw_input("Select Type 1: Json, 2: Direct input, choose 1 or 2: ")
if choice == "1":
    import json
    #print(json.__file__)
    #from pprint import pprint
    with open('payment.json') as data_file:
        data = json.load(data_file)
    i=0
    count = len(data)
    objects = []
    for i in range(count):
        obj = Payment(data[i]['firstname'],
        data[i]['lastname'], data[i]['rate'],
        data[i]['time'], data[i]['extra'] )
        objects.append(obj)
        print(objects[i].getName())
        print(objects[i].getPayment())
        #print("Date: ", data[i]['date'])
        #d = date.fromordinal(data[i]['date'])

else:
    firstname = raw_input("Type First Name: ")
    lastname = raw_input("Type Last Name: ")
    #rate = int(raw_input("Rate: "))
    time = int(raw_input("Time: "))
    #extra = int(raw_input("Additional Fee: "))
    checkname = firstname+lastname.lower()
    #checkname = checkname.strip()

    #checkname = firstname+lastname.ascii_lowercase()
    checkname = checkname.replace(" ", "")
    
    if(checkname.lower() == "mihoyoneda"):
        rate = 12
        extra = 0
    elif(checkname.lower() == "chihirosanga"):
        rate = 10
        extra = 0
    elif(checkname.lower() == "yukikomaeda"):
        rate = 15
        extra = 20
    else:
        rate = int(raw_input("Rate: "))
        extra = int(raw_input("Additional Fee: "))

    obj = Payment(firstname, lastname, rate, time, extra)
    print(obj.getName())
    print("Total Payment: ", obj.getPayment())

#print('Here, done')
