# 접근) 기저조건 : len(a) <= 1 , 재귀조건 : pivot, a[1:]

def paper(r, c, size):
    global N, a,blue,white
    if size == 1: 
        if a[r][c] ==1:
            blue +=1
        else:
            white+=1
        return
    for i in range(r,r + size):
        for j in range(c,c+size):
            if a[i][j] != a[r][c]: 
                for nr, nc in [(r, c), (r, c + (size // 2)), (r + (size // 2), c), (r + (size // 2), c + (size // 2))]:
                    paper(nr,nc,size//2)
                return
    if a[r][c] ==1:
        blue+=1
    else:
        white+=1 

def main():
    global N, a,blue,white,size
    N = int(input())
    a = [[]]
    for i in range(N): 
        temp = list(map(int,input().split()))
        a.append([0]+temp)
    blue = 0
    white = 0 
    paper(1,1,N)
    print(white)
    print(blue)

if __name__ == '__main__':
    main()

'''
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1

9
7
'''