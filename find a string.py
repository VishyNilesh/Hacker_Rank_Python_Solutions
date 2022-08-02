def count_substring(string, sub_string):
    i=0
    pos=0
    value=0
    while i!=-1:
        i=string.find(sub_string,pos,len(string))
        if i!=-1:
            pos=(i+len(sub_string))-1
            value=value+1
    return value


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)