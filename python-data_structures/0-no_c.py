# A function that removes all characters c and C from a string

def no_c(my_str):

    # Initialize an empty string
    result = ""

    # Iterate through each character in the result string
    for char in my_str:

        # Check if the character is c and C
        if char != 'c' and char != 'C':

            # append it to the result string
            result += char

    return result
