# 이진탐색 (조건이 가능(최소 나무길이 확보)하면 계속 높여야 함)
#1.배열초기화 (리스트,lo,hi)
#2.mid값 
#3.check --> lo값 올림 
#4.check N  -- > hi값 내림 
#5.check 조건 설정 

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
import copy
from itertools import *

def check(mid):
    cur = mid #보유금액 
    cnt = 1 # 최초입금시 1회 
    for i in A:
        print('cur,i',cur,i)
        if cur >= i: # 보유금액이 사용금액보다 클경우 
            cur -= i # 보유금액 차감  

        else: # 보유금액이 사용금액과 같거나 더 작은 경우 
            cur = mid #용돈으로충전 
            cur -= i # 남은 금액은 통장에 집어넣고 다시 K원을 인출
            cnt += 1 #인출회수증가

        # print('i,cur,cnt',i,cur,cnt)

    return cnt >= 5 # cnt 5이상이면 True (용돈을 높여야함)

        
def main():
    global N,M,A
    N,M = map(int,read().rstrip().split())
    A = []
    for i in range(N):
        A.append(int(read().rstrip()))

    lo = 1 # 최솟값보다 더 적게 인출할 경우 7일동안 인출회수 5회 초과
    hi = sum(A) # 전체 금액보다 더 많이 인출할 경우 1회만 인출하게 됨 

    while lo <= hi:
        mid = (lo+hi) //2 #중간값에서 시작 
        # print('mid',mid)
        if check(mid): #check결과(인출회수)가 5회이상이면  
            lo = mid+1 # 용돈금액을 높임 조건에 안걸리면 최종 mid가 답임 
            res = mid 

        else:
            hi = mid-1 #인출회수가 5회보다 작을경우 옹돈을 낮추고 

    print(res) 

    
main()

'''
7 5
100
400
300
100
500
101
400

500

1. 필요금액 : 7개
1. 인출횟수 : 5번 
2. 부족하면 0으로 세팅후 인출 
3. 가능하면 check Y ==> hi 를 낮춤 

문제
현우는 용돈을 효율적으로 활용하기 위해 계획을 짜기로 하였다. 현우는 앞으로 N일 동안 자신이 사용할 금액을 계산하였고, 
돈을 펑펑 쓰지 않기 위해 정확히 M번만 통장에서 돈을 빼서 쓰기로 하였다. 
현우는 통장에서 K원을 인출하며, 통장에서 뺀 돈으로 하루를 보낼 수 있으면 그대로 사용하고, 
모자라게 되면 남은 금액은 통장에 집어넣고 다시 K원을 인출한다. 다만 현우는 M이라는 숫자를 좋아하기 때문에, 
정확히 M번을 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원을 인출할 수 있다. 
현우는 돈을 아끼기 위해 인출 금액 K를 최소화하기로 하였다. 현우가 필요한 최소 금액 K를 계산하는 프로그램을 작성하시오.

입력
1번째 줄에는 N과 M이 공백으로 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ M ≤ N)

2번째 줄부터 총 N개의 줄에는 현우가 i번째 날에 이용할 금액이 주어진다. (1 ≤ 금액 ≤ 10000)

출력
첫 번째 줄에 현우가 통장에서 인출해야 할 최소 금액 K를 출력한다.

'''