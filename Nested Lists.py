if __name__ == '__main__':
    x=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l=[]
        l.append(name)
        l.append(score)
        x.append(l)
    scores=[]
    for i in x:
        for j in i:
            scores.append(j[1])
    lowest_score=min(scores.sort())
        