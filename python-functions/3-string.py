#!/usr/bin/env python3
def reverse_string(string):
  return string[::-1]
print(reverse_string)

reverse_string = __import__('3-string').reverse_string
print(reverse_string("Hello"))
print(reverse_string(""))
print(reverse_string("madam"))
print(reverse_string("Hello, World!"))