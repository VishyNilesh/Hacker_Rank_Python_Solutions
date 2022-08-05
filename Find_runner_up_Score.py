if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x=sorted(arr)
    lwd=[]
    for item in x:
        if item not in lwd:
            lwd.append(item)
    print(lwd[-2])
