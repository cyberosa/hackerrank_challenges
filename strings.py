def split_and_join(line):
    # write your code here
    w = line.split()
    w = "-".join(w)
    return w

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)