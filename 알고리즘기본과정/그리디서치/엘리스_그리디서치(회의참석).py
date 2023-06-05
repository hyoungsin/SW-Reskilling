#그리디탐색
#1.회의끝나는 시간 기준 정렬 
#2.끝나는 시간 계속 update

import sys
read = sys.stdin.readline
N = int(read().rstrip())
A = []
for i in range(N):
    A.append(list(map(int,read().rstrip().split())))


A = sorted(A,key = lambda x : x[1],reverse=False)

# print(A)
# print(A[0][0])

end = -1e9
cnt = 0
for i in range(N):
    # print('A[i][0]:',A[i][0])
    if A[i][0] >= end:
        # print (A[i][0])
        end = A[i][1]
        cnt += 1

print(cnt)

'''
접근 : sorted, cnt, end_date
디버깅 : i[0] >= end_time

5
1 4
3 5
2 7
4 6
7 8

3

1.무슨기준으로 정렬해볼까? (시작점, 끝점 , 길이? ) -> full time meeting은 맨뒤로 변경함 
2. 첫미팅은 무조건 시작해야 하고 (제일빨리 끝남) 둘째 미팅부터는 시작점이 첫째 meeting완료보다 큼
'''