################
#1.배열초기화 / visited (겹침check)
#2 1번부터 9번색깔까지의 최소/최대 좌표찾기 
#3.min_r/c ~ max_r/c 배열에서 해당숫자가 아닌값이 나오면  아닌 숫자의 r/c를 1개 더함 
#4.1번만 visited인 갯수를 찾음 

import sys 
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(read().rstrip())
A = []
for i in range(N):
    A.append(list(map(int,read().rstrip())))
    
visited = [0 for i in range(10)] #1.배열초기화 / visited (겹침check)

for i in range(1,10): 
    min_r = 1e9 
    min_c = 1e9
    max_r = -1e9
    max_c = -1e9
    for r in range(N):
        for c in range(N):
            if A[r][c] == i:
                min_r = min(min_r,r)
                min_c = min(min_c,c)
                max_r = max(max_r,r)
                max_c = max(max_c,c)

    if min_r == 1e9 or min_c == 1e9 or max_r == -1e9 or max_c == -1e9:
        continue
    
    visited[i] += 1 #해당숫자좌표 update되었으면 1로 수정 

    # print('i,visited',i,visited)

    for r in range(min_r,max_r+1):
        for c in range(min_c,max_c+1):

            if A[r][c] != i:
                visited[A[r][c]] += 1 
                # print('i, r,c, A[r][c],visited:',i, r,c, A[r][c],visited)
                
print(visited.count(1))




################
#1.배열초기화 / visited (겹침check)
#2 1번부터 9번색깔까지의 최소/최대 좌표찾기 
#3.min_r/c ~ max_r/c 배열에서 해당숫자가 아닌값이 나오면  아닌 숫자의 r/c를 1개 더함 
#4.1번만 visited인 갯수를 찾음 



'''
4
1230
1737
1777
0220

2

N : 정사각형 가로세로크기
색정보(1~9)까지 위치정보가주어진다. 0번을 색칠 안된 상태 
덧칠하지 않은 번호 찾아서 갯수 출력 

'''