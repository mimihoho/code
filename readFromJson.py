#try:
#    import json
#except ImportError:
#    import simplejson as json
import json
#print(json.__file__)
from pprint import pprint

with open('payment.json') as data_file:
    data = json.load(data_file)
    print(len(data))

#print('Here')
#pprint(data)
#print('done')
