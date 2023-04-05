
# ### handling exceptions
# x = input("Enter number1: ")
# y = input("Enter number2: ")
# try:
#     z = int(x) / int(y)
# except Exception as e:
#     print("exception ocurred: ",e)
#     z = None
# print("Division is: ", z)

### raise exceptions
class Accident (Exception):
    def __init__(self, msg):
        self.msg=msg
    def print_exception(self):
        print ("User defined exception: ", self.msg) 
            
try:
    raise Accident('crash between two cars')
except Accident as e: 
    print(e)


# ### dictionaries & tuples 
# """
# It allows you to store key value pair. Telephone directory
# To get the value from a dictionary we must use the square bracket 
# """

# directory = {"tom:": 12345, "rob:":54321, "tonny:":67890}
# print(directory)

# directory["pili:"] = 54321
# print(directory)

# del directory["tonny:"]
# print(directory)

# for key in directory:
#     print("key:", key, "value:", directory[key])
#     print(key, directory[key])

# print("tom:" in directory)
# directory.clear()
# print(directory)

# ### tuples: list of values grouped together. in tuples values are heterogeneous.
# ###tuples are imnmutable. 

# point=(5,9)
# print(point[1])

# ### functions
# # block of code that preforms a task. Like dishwashing. Input.....add water
# # ....detergent.......turn on....OUTPUT......Clean dishes. 

# # def calculate_total(exp): ##exp is a local variable for this function.
# #     """
# #     This function takes two arguments which are integer numbers and it will 
# #     return sum of them as an output
# #     """
    
# #     total = 0
# #     for item in exp:
# #         total+=item
# #     return total

# ### lists: in lists values are homogeneous
# # list_1 = [2100, 3400, 3500]
# # list_2 = [200, 500, 700]

# # list_1_total = calculate_total(list_1)
# # list_2_total = calculate_total(list_2)

# # print("list_1 sum:", list_1_total)
# # print("list_2 sum:", list_2_total)

# # total = 0 
# # def sum(a,b = 0):
# #     print("a:", a)
# #     print("b:", b)

# #     total = a+b 
# #     print(total)
# #     return total

# # n = sum(a=4)
# # print(total)

# # ### for loop:
# # rent = 2500
# # food = 1000
# # utilities = 900
# # transport = 800
# # gastos = [2300, 1000, 900, 800]
# # expenses = [rent, food, utilities, transport]
# # print(expenses)

# # total = 0
# # for i in range(len(expenses)):
# #     print('Month:', (i + 1), 'Expense:', expenses[i])
# #     total += expenses[i] 

# # # total = 0
# # # for item in expenses:
# # #     total += item
# # # print(total)    

# # ##break

# # key_location = "chair"
# # locations = ["garage", "living room", "chair", "closet", "garden"]
# # for i in locations:
# #     if i==key_location:
# #         print("key has been found in", i)
# #         break
# #     else:
# #         print("keys not found in", i)   

# # ##continue
# # for i in range(1, 6):
# #     if i%2==0:
# #         continue
# #     print(i*i)

# # ##while    
# # key_location = "garage"
# # locations = ["garage", "living room", "chair", "closet", "garden"]
# # for i in locations:
# #     if i==key_location:
# #         print("key has been found in", i)
# #         break
# #     else:
# #         print("keys not found in", i)       



# ### if statement:

# #num = input("Enter a number: ")
# # #num = int(num)

# # indian_dishes = ["samosa", "daal", "naan"]
# # chinese_dishes = ["egg role", "pot sticker", "fried rice"]
# # italian_dishes = ["pizza", "pasta", "risotto"]

# # dish = input("Enter a dish name:")

# # if dish in indian_dishes:
# #     print("indian")
# # elif dish in chinese_dishes:
# #     print("chinese")    
# # elif dish in italian_dishes:
# #     print("italian")
# # else:
# #     print("Based on little knowledge I have I can't tell you where this dish is from")        

# # if num%2!=0:
# #     print("number is even")
# # else:
# #     print("number is odd") 



# # ### functions in python

# # def budget():
# #     rent= 1200
# #     food = 300
# #     internet = 200
# #     print(internet+food)

# # ### numbers in python

# # print(12 % 7)

# # print(10*23+20) 

# # ### Strings in python

# # text = "ice cream"
# # print(text)
# # print(text[1:])


# # w1 = 'hello'
# # w2 = 'world'
# # join = w1 + ' ' + ' ' + w2
# # print(join)

# # states = 'total states in usa:'
# # number = 52
# # total = states + ' ' + str(number) 
# # print(total)

# # ### listst in python
# # groceries = ['bread', 'pasta', 'fruits', 'shampoo', 'wipes']
# # print(groceries)
# # print(groceries[0])

# # groceries += ['chips']
# # print(groceries)

# # groceries.insert(1, 'butter')
# # print(groceries) 
# # print(groceries[0], groceries[4])

# # groceries.append('beans')
# # print(groceries)

# # print(len(groceries))
# # print('avocado' in groceries)

# # print(not 5 == 4 and 4<5)

