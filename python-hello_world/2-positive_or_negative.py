#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
  print("{} is postive".format(number))
if number == 0:
  print("{} is zero".format(number))
if number < 0:
  print("{} is negative".format(number))

