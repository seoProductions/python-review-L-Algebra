# reviewing python after 4 long years 
# below is a long long long list of commands, trial and error,
# and descriptions of the python language. Lots of details 
# I had to cover. Take a look if you want :)


#input() #returns string by default
# cast input() using float() or int() constructor

l = k = j = 1
# is equivilent to
j = 1
k = j
l = k

#swaping values can be done like this
#this helps avoid creating a temporary value, which comes much in handy
j, k = k, j


## python operands

a = 3 + 7
a //= 2
print( a / 2 )  # float division. aka TRUE (realistic) division
print( a // 2)  # int division.   aka FLOOT (truncated) division

# tip - make numbers more readable using underscores!

a = 234234_234234.2122222_33333
print(a)

# exponentiation
a = 5
a ** 3
print(a)



#########
#########
#########
#########
#########
#########

import random

b = random.randint(4, 8) #inclusive
print(b)

b = random.randrange(4,8) #exclusive 8. generates nubmer from 4 to (8-1)
print(b)

#generate random float from 0 to 1, just like in c++
b = random.random()
print(b)

#set the random seed using
b = random.seed(2342)

# printing using commas

print(b, a, j, l, k)

if j + k >= 0:
    print("the sum of j and k are greater than 1!!!!, their sum is ", j+k)

import sys
#optional exit with exit code!!! wow
#sys.exit(1)

#conditional expressions
# turn this

if (l == 1):
    j = 23
else:
    j = 0

#into this
#THIS IS PYTHONS VERSION OF A TERNARY OPERATOR ?: !!!!!!!!!!!!!! very much english like!

#j = 2  if l == 1 else j = 0

#def max(n1, n2):
#    return n1 if n1 > n2 else n2

#print("The max value from l, k, j, a, and b is: ", max(l, max(k, max(j, max(a, b)))))

# return -1 or 1 only
import time

random.seed(time.time())
print("random int is now ", -1 if random.randint(0,1) == 0 else 1)

#switch statement equivilent for python
month = 2

match month:
    case 1: print("January")
    case 2: print("February")
    case 3: print("March")

#math functions
import math
print(math.sqrt(2))
print(math.atan(math.pi))

#strings in python are simple. You can delcare them using either ' ' or " "

str = "hi"
str = "empty string below me"
str = ""
str = 'also delcare with single quotes!'
str = ''

#convention is to use single quotes for char, and double quotes for any other string
convention = "string"
convention = 'a'    #char

# python uses unicode to represent characters

char = "9"
print(ord(char)) # will print out b

char = 88
print(chr(char)) # will print the uni-code value/ ASCII value

#you can also format print statements by overriding the default end variable of 
# end = "\n"

print("hey", end="\t")
print("hey", end="\t")
print("hey", end="\t")
print("hey", end="\t")
print("hey", end="\t")
print("hey", end="\t")
print("just wanted to say hi!")

#python has a way of checking if a certain substring exists within a string
#these operators evaluate into a boolean expression, being True of False

str = "the other ones are in the other"

print("lol" not in str) # >>> True
print("he" in str)      # >>> True
print("the" not in str) # >>> False


# instead of printing you can use f strings!


print(f"f strings are more avaliable")
print(f"and you can include variables like this one : {a} and this one : {j}")

str = "poaijwdfpojaiwdf"
print(f"starting from the third index, the string above is the following: {str[3:]}")

#you can technically use format like this

print(format("lol this is formated", "12"))


# here is an example of nubmers arranged nice and neatly
a = 12111.123427
print(format(a, ">20.5f"))
a = 432666.123234427
print(format(a, ">20.5f"))
a = 122222221121.123234234427
print(format(a, ">20.5f"))
a = 121111.1234234234234234122347
print(format(a, ">20.5f"))
a = 121123421.122343427
print(format(a, ">20.5f"))


## classes overview

class TrafficLight:
    def __init__(self):
        self.state = "red"
        self.syncedWith = None

    def turnGreen(self):
        if self.state == "red":
            self.state = "green"
    def turnYellow(self):
        if self.state == "green":
            self.state = "yellow"
    def turnRed(self):
        if self.state == "yellow":
            self.state = "red"
    

    def isGreen(self):
        return True if self.state == "green" else False

    def canCross(self):
        return self.isGreen() or self.state == "yellow"

    def syncWith(self, TrafficLight_in):
        self.syncWith = TrafficLight_in
        TrafficLight_in.syncWith = self
        self.state = TrafficLight_in.state
    

light1 = TrafficLight()
print(f"is the light green? the answer is: {light1.isGreen()}")
light1.turnGreen
print(f"is the light green? the answer is: {light1.isGreen()}")

light1.turnYellow()
print(f"can car1 cross now?   {light1.canCross()}")


light2 = TrafficLight()
light2.turnGreen()
print(f"can car2 cross now?   {light2.canCross()}")

light2.turnRed()
print(f"can car2 cross now?   {light2.canCross()}")
print("\n\n\n\n\n")

syncedWith = TrafficLight()
syncedWith.syncWith(light1)
light2.syncWith(light1)


print(f"can car1 cross now?   {light1.canCross()}")
print(f"can car2 cross now?   {light2.canCross()}")
print(f"can car3 cross now?   {syncedWith.canCross()}")


## now changing one light's status to see if all others change and if synced up correctly

light2.turnGreen()
print("\n", end="")

print(f"can car1 cross now?   {light1.canCross()}")
print(f"can car2 cross now?   {light2.canCross()}")
print(f"can car3 cross now?   {syncedWith.canCross()}")



#############################
#############################
#############################

# Now to move on to python functions
# 90% of the concepts are the same, its simly the 
# details that differ, lets take a look

#define functions using "def" keyword

def function():
    print(f"inside the function")

def f(a, b):
    print(a, b)
#and invoke
function()
f(9,8)


# just about all variables in python are 
# OBJECTS
# Python passes these via reference!!!!

n1 = 4
n2 = 5

f(n1, n2) #both n1,n2 and a,b both reference the same int object

def printID(a):
    return id(a)


#BOTH WILL BE THE SAME!!!!!!!!!!!!!!!!
print(f" id of n1 is {id(n1)}", end="\n\n")
print(f" id of n1 passed by ref inside function is {printID(n1)}", end="\n\n")

def intObjectAreImmutible(a):
    # value of a is no longer the same, thus new int object will be created
    # and it's ID will change bc its no longer a reference 
    a += 1
    return id(a)

print(f" id of n1 is {id(n1)}", end="\n\n")
print(f" id of n1 modified inside function is  {intObjectAreImmutible(n1)}", end="\n\n")


###############################################

#python has a "NONE" keyword for void functions

def voidFunction2():
    return

def voidFunction1():
    return None 

print(f" void function will return this value: {voidFunction2()}")
print(f" void function will return this value: {voidFunction1()}")

######
## Positional Arguments
#####

#just like in c++ and other languages

def positional(a, b, c, d):
    return
positional(3,4,2,3)         ## MUST BE IN ORDER


######
## Keyword Arguments
#####

#python specific, pass arguments like a key=value pair!

def keyword(a, b, c, d):
    return
keyword(c=2, b=2, d=2, a=4)
keyword(c=6, b=2, d=9, a=4)    # YOU ARE ALLOWED TO DO THIS

#####
## Default arguments
####

#the same as c++ and others

def defaultargs(a = 20, b = 2):
    return
defaultargs()
defaultargs(3)
defaultargs(23, 3)
defaultargs(b = 3)
defaultargs(b = 23, a=3)        # VERY FLEXIBLE, PYTHON IS VERY LAID BACK


#################################################3
#################################################3
#################################################3
#################################################3
#################################################3

#how to acess other python files????!?!?!?! use this syntax

from Rectangle import Rectangle # import class only
from Rectangle import *     #import all classes, modules, and functions
r = Rectangle(3,2)
print(f"area is {r.getArea()}")

# alternative syntax

import Rectangle
#   file    .  class
r1 = Rectangle.Rectangle(5,2)
print(f"area is {r1.getArea()}")


#####################
#####################

# Local and Global Scopes are just about the same, but
# python doesent create a scope in CONTROLL BLOCKS

# CONTROLL BLOCKS: IF() WHILE() CASE()......



if 1 == 1:
    y = 2

print(y) # will print, because if() statement does not create a scope


# ONLY FUNCTIONS, CLASSES, and MODULES CREATE A SCOPE

def globalkeyword():
    #will bind this variable to global y
    global y
    print(y)
    # this really helps readability

""" WILL NOT WORK, global only binds local variable


def globalkeyword():
    global zebra
    zebra = 3
    return


print(zebra)

"""

# This has no effect, zebra is already global by default
global zebra
zebra = 3
print(zebra)



# Good practice to modularize code and use abstraction :)

from Constants import *

print(f"PI is {PI}")
print(f"E  is {E}")
print(f"PHI is {Phi}")

# I perfer this:

import Constants

print(f"PI is {Constants.PI}")
print(f"E  is {Constants.E}")
print(f"PHI is {Constants.Phi}")

