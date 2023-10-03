# x, z = 0, 1
# while(z < 30):
#   print(z)
#   x, z = z, x+z 

  # 1, 1, 2, 3, 5, 8, 13

# a, b = 0, 1

# while (b < 1000):
#   print(b, end="\n")
#   a, b = b, a+b


#!/usr/bin/env python3
# Write a function that removes all characters c and C from a string.

# def no_c():
#   my_string = input("Enter strings to remove all c and C from strings")

#   my_string.replace("c", "a")
#   print(my_string)
# no_c()

# def no_c(my_string):
#     result = ''
#     for char in my_string:
#         if char not in ('c', 'C'):
#             result += char
#     return result

# # Test
# print(no_c("Concert is an amazing time to come together in children of God"))

def no_c(my_string):
  new_string = ''

  for i in my_string:
    if i not in ('c', 'C'):
      new_string += i
  return new_string

# Function to remove all c and C from strings

# Test the function
if __name__ == "__main__":
    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))