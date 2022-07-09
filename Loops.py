if __name__ == '__main__':
    n = int(input())
if(n in range(1,21)):
    val=[]
    i=0
    while(i<n):
        val.append(i)
        i+=1
for i in val :
    print(i**2)