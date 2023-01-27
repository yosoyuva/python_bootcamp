import sys

def reverse_swap_case(string):
    # Reverse the string
    reversed_string = string[::-1]
    # Swap the case of the characters
    swapped_string = reversed_string.swapcase()
    return swapped_string

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Merge the arguments into a single string separated by spaces
        input_string = ' '.join(sys.argv[1:])
        print(reverse_swap_case(input_string))
    else:
        print("Please provide a string as argument")
