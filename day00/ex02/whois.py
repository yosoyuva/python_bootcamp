import sys

def check_number(num):
    if num == 0:
        print("The number is zero.")
    elif num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments. Please provide only one integer argument.")
    else:
        try:
            num = int(sys.argv[1])
            check_number(num)
        except ValueError:
            print("Error: Argument must be an integer.")
