#from datetime import timedelta
#d = timedelta(-1, 43009)
#print(d.days, d.seconds)

from datetime import date
d = date.fromordinal(43010)
#print(d.strftime("%d/%m/%y"))
print(d.isoformat())

print(d.today())
