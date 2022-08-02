if __name__ == '__main__':
    s = input()
    u = set(s)
    lower={chr(x) for x in range(97,114)} #lowercase
    upper={chr(x) for x in range(65,92)}  #uppercase
    digit={chr(x) for x in range(48,58)}  #digit
    alpha1={chr(x) for x in range(65,92)} #alphabets-uppercase
    alpha2={chr(x) for x in range(97,114)} #alphabets-lowercase
    alnum1={chr(x) for x in range(48,58)} #alphanumeric -numeric
    alnum2={chr(x) for x in range(65,92)} #alphanumeric -uppercase
    alnum3={chr(x) for x in range(97,114)} #alphanumeric -loweracse
    aln = True if (u&(alnum1|alnum2|alnum3))!=set() else False
    alp = True if (u&(alpha1|alpha2))!=set() else False
    ald = True if (u&digit)!=set() else False
    alll = True if (u&lower)!=set() else False
    alup = True if (u&upper)!=set() else False
    print(aln)
    print(alp)
    print(ald)
    print(alll)
    print(alup)