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
last = number % 10
s_num = "Last digit of"
fi_ve = "and is greater than 5"
six_zero = "and is less than 6 and not 0"
if (last > 5):
    print(f"{s_num} {number} is {last} {fi_ve}")
elif (last == 0):
    print(s_num + " {} is {} and is 0".format(str(number), str(last)))
elif (last < 6 and last != 0):
    last = abs(number) % 10
    neg_last = -last
    print(f"{s_num} {number} is {neg_last} {six_zero}")
