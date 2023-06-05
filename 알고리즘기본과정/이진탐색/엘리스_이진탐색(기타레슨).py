# 이진탐색
#1.배열 초기화 (리스트,min,max)
#2.while 문 구성 (mid)
#3.탐색조건 설정 (lo/hi)
#4.Check함수 구성 

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
import copy
from itertools import *

def check(mid):
    cnt = 1 # 최초 cnt1개 
    sum = 0 # 블루레이에 담긴 비디오길이
    for i in A:
        if sum+i <= mid: # 비디오길이의 누적합계가 블루레이보다 작거나 같으면 
            sum += i #블루레이에 담음 

        else: # 누적 i sum이 mid값을 초과할 경우 
            cnt += 1 # cnt를 1나 추가하고 
            sum = 0 # 빈 블루레이를 준비한후 
            sum += i # 다음순서를 담음 
    
    return cnt <= 3 # 블루레이 개수가 3개 

def main():
    global A
    N,M = map(int,read().rstrip().split())
    A = list(map(int,read().rstrip().split()))

    lo = min(A) # 가장큰 비디오는 담을수 있어야 함 
    hi = sum(A) # 전체합일 경우 블루레이 1개 필요 그 이상은 모두 1개 

    while lo <= hi: #중간값이 lo ~ hi까지 모두 탐색 
        mid = (lo+hi)//2
        if check(mid):
            hi = mid-1 # 블루레이 개수가 3개이하일경우 숫자 줄임
            res = mid # 동일할때 최종 값이 res임 
        else:
            lo = mid+1 # 블루레이 개수가 3개 초과할 경우 블루레이 크기 느림

    print(res)

main()

'''

9 3
1 2 3 4 5 6 7 8 9

17

[입력]

9 : 강의수 
3 : 3개의 블루레이에 강의 담음 (강의는 이어짐)
블루레이의 길이가 최소가 되도록 함  


입력
강의수 : N (1 ≤ N ≤ 100,000), M (1 ≤ M ≤ N)
기타 강의의 길이 (강의 순서대로 분 단위로(자연수)로 주어진다.( 각 강의의 길이는 10,000분을 넘지 않는다.) 

출력
가능한 블루레이 크기중 최소를 출력한다.

힌트
강의는 총 9개이고, 블루레이는 총 3개 가지고 있다.
1번 블루레이에 1, 2, 3, 4, 5, 2번 블루레이에 6, 7, 3번 블루레이에 8, 9 를 넣으면 각 블루레이의 크기는 15, 13, 17이 된다. 
블루레이의 크기는 모두 같아야 하기 때문에, 블루레이의 크기는 17이 된다. 17보다 더 작은 크기를 가지는 블루레이를 만들 수 없다.

'''