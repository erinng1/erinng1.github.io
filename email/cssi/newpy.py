''' import math
import random

def say_hello() :
    print "Hello!"
    print "It\'s Thursday!"

def print_info(text) :
    print "Value is " + text

#say_hello()
#print_info("June is almost over.")
#print_info("What are you doing for July 4th?")

def calPower(base, power):
    answer = 1;
    for i in range(power):
        answer = base**power;
    return answer;

#print calPower(4, 2)
#print calPower(3, 5)
#print calPower(int(raw_input("Base?")), int(raw_input("Power?")))
#print math.pow(5,3) '''

groceries_by_price = {
    'Eggs' : 2.59,
    'Milk' : 3.19,
    'Butter' : 2.69,
    'Yogurt' : 3.19
    }
for item in groceries_by_price:
	print item + ' ' + str(groceries_by_price(item))
