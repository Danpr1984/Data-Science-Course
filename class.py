# ###Class

# class Human:
#     def __init__(self, n, o):
#         self.name = n
#         self.occupation = o

#     def do_work(self):
#         if self.occupation == "tennis player":
#             print(self.name, "plays tennis")
#         elif self.occupation == "actor":
#             print(self.name, "shoots a film")
#         else:
#             print(self.name, "is a ", self.occupation)
#     def speaks(self):
#         print(self.name, "says how are you?")

# # tom = Human ("tom cruise", "actor")
# # tom.do_work()
# # tom.speaks()

# maria = Human("maria sharapova", "teacher")
# maria.do_work()
# maria.speaks()

### inheritance

# class Vehicle:
#     def general_usage(self):
#         print("general use: transportation")

# class Car(Vehicle):
#     def __init__(self):
#         print("I am car")
#         self.wheels = 4
#         self.has_roof = True

#     def specific_usage(self):
#         print("specific use: commute to work, vacation with family")        

# class Motorcycle(Vehicle):
#     def __init__(self):
#         print("I am bike")
#         self.wheels = 4
#         self.has_roof = True

#     def specific_usage(self):
#         print("specific use: roadtrip and racing")


# c = Car()
# c.general_usage()
# c.specific_usage() 

# m = Motorcycle()
# m.general_usage()
# m.specific_usage()

# print(isinstance(c, Motorcycle))

### Multiple inheritance

class Father():
    def gardening(self):
        print("I enjoy gardening")

class Mother():
    def cooking(self):
        print("I enjoy cooking")

class Child(Father, Mother):
    def sports(self):
        print("I enjoy sports")

c = Child()
c.gardening()
c.cooking()
c.sports()