#for loop printing 1-99 
for num in range(100):
    print("{:d}".format(num), end=", " if num < 99 else "\n")