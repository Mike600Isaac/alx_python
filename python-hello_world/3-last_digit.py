#!/usr/bin/python3
# import random
# number = random.randint(-10000, 10000)
# YOUR CODE HERE
# last_digit = number % 10
# if (last_digit > 5):
#    print("Last digit of {0} is {1} and is greater than 5".format(number,last_digit))
# if (last_digit == 0):
#    print("Last digit of {0} is {1} and is 0 ".format(number,last_digit))
# last = abs(number) % 10
# neg_digit = -last
# if (neg_digit < 6 and neg_digit != 0):
#   print("Last digit of {0} is {1} and is less than 6 and not 0".format(number,neg_digit))

#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10  # We use abs to ensure that negative numbers also give positive last digits

print("Last digit of", number, "is", last_digit, end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:  # last_digit is less than 6 and not 0
    print("and is less than 6 and not 0")

