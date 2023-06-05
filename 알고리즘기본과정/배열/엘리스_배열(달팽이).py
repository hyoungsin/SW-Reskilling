
# 접근 : 1.n,a,r,c(-1),d,cnt,step 2.while step>0,c+=d,a[r][c]=cnt, cnt+=1, step-=1, 3.i,j,a[i][j]) 

def main():
    n = int(input()) # n 정수 입력 
    a = [[0 for j in range(n)] for i in range(n)] # 빈배열 생성
    r = 0       # 행
    c = -1      # 열
    d = 1       # 방향
    cnt = 1     # 숫자 찍을 변수
    step = n    # 출력할 때 사이즈 기억 하고 있어야 되어서 따로 저장
    while step > 0: # 최초 step은 4 1씩 줄여나감
        for i in range(step):
            c += d # 우측으로 이동
            a[r][c] = cnt #최초 (0,0)
            cnt += 1 # 우측 1칸씩 이동
        step -= 1 # 4번 반복하고 3으로 줄임    
        for i in range(step):
            r += d # 아래로 이동
            a[r][c] = cnt # 최초 위치 (1,3)
            cnt += 1
        d *= -1 # 방향 전환 (d = d*-1)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end= ' ') # a좌표의 위치반복 표시 
        print() #줄바꿈 

if __name__ == '__main__':
    main()


'''
4

1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7


'''