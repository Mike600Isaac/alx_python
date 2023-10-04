#!/

# Simplest class example created
# class Person:
#   pass        # An empty block

# p = Person()  # Object of the class Person
# print(p)      # print the instant of the class


# # Method of the class: created
# class Salutation:                            # class created
#   def greet(self):                          # method of the class created
#     print("Good Morning People!", end="\n") # print function
# p = Salutation()                             # object of class instantiated

# p.greet()




# # Using __init__ method: this is used for the initialisation(passing initial value to object) you want to do with object

# class Salutation:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def greet(self):
#     print("My name is {}, I am {} years old".format(self.name, self.age))
#     print()

# p = Salutation("JESUS CHRIST THE SON OF GOD", "FOREVER")
# p.greet()
# # Salutation("Isaac Micheal", 28).greet()


# class Robot:

#   """This is a CLASS variable declaration been done HERE!"""
#   population = 0

#   """This is initization of object argument been done HERE!"""
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#     """Initializes data"""
#     print("Initializing {} at age {}".format(self.name, self.age))


#     """Once the person is created, the Robot. Then add to population"""
#     Robot.population += 1

# def live(self):
#   """I am Living"""
#   print("{} is been given more Life".format(self.name))

#   """This remove the population when a person is created"""
#   Robot.population -= 1

#   if Robot.population == 0:
#     print("{} was the last one.".format(self.name))
#   else:
#     print("There are still {:d} Robot working.".format(Robot.population))

# def say_hi(self):
#   """Greeting  by the robot

#   Yeah they can do that"""

#   print("Greetings my master will call me {}".format(self.name))

# @classmethod
# def how_may(cls):
#   """Print the current
   
#      population"""
#   print("We have {:d} robots.".format(cls.population))



class Square:
    def __init__(self, size):
        self.__size = size

my_square = Square(3)

print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

