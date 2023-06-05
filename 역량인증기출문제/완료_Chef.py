#####
#1.배열 초기화
#2.배열 정렬 (내림차순)
#3. 1번째 값이 더 큰것 누적 

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    N = int(read().rstrip())
    A = []
    for i in range(N):
        A.append(list(map(int,read().rstrip().split())))

    su = [] # 변수명 주의 (sum충돌)
    for i in A:
        su.append(i[1])
    ma = max(su)
    visited = [0 for i in range(ma+1)] # 여러구역 순회 필요하면 visited활용 

    A = sorted(A,key = lambda x: x[1]) # 뒤에요소 기준 정렬 (오름차순)

    for price,time in A: # 손님 정보 추출 
        for i in range(time,0,-1): # 2,1,0 순으로 점검

            if visited[i] == 0 : # 예약 시간이 비어 있으면 단가 입력 (중복예약이 없으면)
                visited[i] = price

                # print('i,visited[i]:',i,visited[i])
                
                break
                
            elif visited[i] < price: # 예약이 중복되고 단가가 더 높다면 
                temp = visited[i]
                visited[i] = price
                price = temp # 더 큰 값으로 갱신하고 작은 값은 price로 보냄

    print(sum(visited))

main()

#####
#1.배열 초기화
#2.배열 정렬 (내림차순)
#3. 1번째 값이 더 큰것 누적 

'''
4
10 3
7 5
8 1
2 1

25

4
6 1
8 2
9 2
10 3

손님수 N 
음식값 Price, 예약희망시간 Time
제약 : 예약 희망시간보다 늦으면 안되고 이르면 ok (더 값이 높아야 함)

'''