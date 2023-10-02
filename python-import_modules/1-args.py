#!/usr/bin/python3
# Write a program that prints the number of and the list of its arguments.

# argparse.py

# import sys

# def main(argv):
#     arg_count = len(argv) - 1  # subtract 1 to exclude the script name itself
    
#     # Print number of arguments
#     if arg_count == 1:
#         print(f"Number of argument: {arg_count}:")
#     elif arg_count == 0:
#         print("Number of arguments: 0.")
#         return  # exit as no further processing needed for 0 arguments
#     else:
#         print(f"Number of arguments: {arg_count}:")

#     # Print each argument with its position
#     for i, arg in enumerate(argv[1:], 1):  # skip the script name at argv[0]
#         print(f"{i}: {arg}")

# if __name__ == "__main__":
#     main(sys.argv)



import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name from the arguments

    num_args = len(argv)
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        print("1:", argv[0])
    else:
        print(f"{num_args} arguments:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}:", arg)

if __name__ == "__main__":
    main()



