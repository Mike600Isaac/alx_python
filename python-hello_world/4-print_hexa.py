#!/usr/bin/python3
#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
# task 3
#!/usr/bin/python3
for i in range(99):
    print("{:d} = 0x{:x}".format(i, i))