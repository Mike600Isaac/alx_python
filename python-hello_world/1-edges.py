#!/usr/bin/python3
word = "Holberton"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print("First 3 letters: {}".format(word[:3]))
print("Last 2 letters: {1}{0}".format(word[len(word)-1], word[len(word)-2]))
word = word[1:]
print("Middle word: {}".format(word[:-1]))