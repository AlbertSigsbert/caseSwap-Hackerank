def swap_case(s):
    new_string = ''

    for char in s:
        if char.islower():
            upper = char.upper()
            new_string += upper
        else:
            lower = char.lower()
            new_string += lower

    return new_string


s = input()[:1000]

value = swap_case(s)
print(value)
