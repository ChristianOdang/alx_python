# A function that returns a tuple with length of a string

def multiple_returns(sen):
    # Length of the sentences
    length = len(sen)

    # First character
    first_char = sen[0] if length > 0 else None
    # return
    return length, first_char
