def split_and_join(line):
    # write your code here
    l=line.split(' ')
    l='-'.join(l)
    return l

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)