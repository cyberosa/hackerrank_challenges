def swap_case(s):
    new_str = ''
    for c in s:
        if c.isupper():
            new_char = c.lower()
        else:
            new_char = c.upper()
        new_str += new_char
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)