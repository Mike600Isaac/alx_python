def main():
  print(reverse_string("Hello"))         # Output: "olleH"
  print(reverse_string(""))              # Output: ""
  print(reverse_string("madam"))         # Output: "madam"
  print(reverse_string("Hello, World!")) # Output: "!dlroW ,olleH"


def reverse_string(string, end=''):
    reversed = string[::-1]
    return reversed
main()