#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:18:27 2024

@author: alex
"""

# class Robot(object):
#     pass

# if __name__ == "__main__":
#     x = Robot()
#     y = Robot()
    
#     x.name = "Marvin"
#     x.build_year = "1979"
#     y.name = "Caliban"
#     y.build_year = "1993"
    
#     print(x.name)
    
#     y2 = y
#     print(y == y2)
#     print(y == x)
    
#     print(x.__dict__)
#     print(y.__dict__)


######################################

# x = Robot()
# Robot.brand = "Kuka"
# print(x.brand)

# y = Robot()
# print(y.brand)

# Robot.brand = "Thales"

# print(x.brand)
# print(y.brand)

# print(x.__dict__)
# print(Robot.__dict__)

# # print(x.energy)
# print(getattr(x, 'energy', 100))

######################################

# def hi(obj):
#     print("Hi, I am " + obj.name)

# class Robot:
#     say_hi = hi
    
# x = Robot()
# x.name = "Alex"
# #Robot.say_hi(x)
# x.say_hi(x)

######################################

# class A:
#     def __init__(self):
#         print("__init__ has been executed!")
# x = A()

# class Robot:
#     def __init__(self, name=None):
#         self.name = name   
#     def say_hi(self):
#         if self.name:
#             print("Hi, I am " + self.name)
#         else:
#             print("Hi, I am a robot without a name")
# x = Robot()
# x.say_hi()
# y = Robot("Marvin")
# y.say_hi()

#######################################

# class Robot:
#     def __init__(self, name=None):
#         self.name = name   
#     def say_hi(self):
#         if self.name:
#             print("Hi, I am " + self.name)
#         else:
#             print("Hi, I am a robot without a name")
#     def set_name(self, name):
#         self.name = name
#     def get_name(self):
#         return self.name
# x = Robot()
# x.set_name("Henry")
# x.say_hi()
# y = Robot()
# y.set_name(x.get_name())
# print(y.get_name())

#######################################

class Robot:
    def __init__(self, 
                 name=None,
                 build_year=2000):
        self.__name = name   
        self.__build_year = build_year
        print(self.__name + " has been created!")
        
    def __del__(self):
        print ("Robot has been destoyed")
            
        
    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")
            
            
            
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name  
    
    def set_build_year(self, by):
        self.__build_year = by
        
    def get_build_year(self):
        return self.__build_year

    def __repr__(self):
        return "Robot('" + self.__name + "', " +  str(self.__build_year) +  ")"    
    
    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " +  str(self.__build_year)
    
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was built in the year " + str(rob.get_build_year()) + "!")
        
    print("Deleting x")
    del x
    print("Deleting y")
    del y
        





