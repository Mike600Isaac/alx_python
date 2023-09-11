#!/usr/bin/env python3
def reverse_string(string):
  reversed = string[::-1]
  return (reversed)

# reverse_string = __import__('3-string').reverse_string
print(reverse_string("Hello"))
print(reverse_string(""))
print(reverse_string("madam"))
print(reverse_string("Hello, World!"))



def reverse_string(string):
    reversed = string[::-1]
    return (reversed)

print(reverse_string("Hello"))         # Output: "olleH"
print(reverse_string(""))              # Output: ""
print(reverse_string("madam"))         # Output: "madam"
print(reverse_string("Hello, World!")) # Output: "!dlroW ,olleH"