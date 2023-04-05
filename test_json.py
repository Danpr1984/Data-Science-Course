book = {}
book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 98989898
}

book['bob'] = {
    'name': 'bob',
    'address': '1 tomatoe street, NY',
    'phone': 1212121212
}

import json
s = json.dumps(book)
print(book['bob']['phone'])

for person in book:
    print(book[person])
 
# # Creating a dictionary
# Dictionary ={1:'Welcome', 2:'to',
#             3:'Geeks', 4:'for',
#             5:'Geeks'}
  
# # Converts input dictionary into
# # string and stores it in json_string
# json_string = json.dumps(Dictionary)
# print('Equivalent json string of input dictionary:',
#       json_string)
# print("        ")
 
# # Checking type of object
# # returned by json.dumps
# print(type(json_string))