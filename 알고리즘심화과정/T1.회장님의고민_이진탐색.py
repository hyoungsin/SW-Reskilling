import sys 
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
global n, a, m,res

def check(mid): 
    global n, a, m,res
    sum = 0 
    for i in a: 
        sum += min(i,mid)
    return sum <= m

def main():
    global n, a, m,res
    n = int(read().rstrip())
    a = list(map(int,read().rstrip().split()))
    m = int(read().rstrip())
    lo = 0 
    # hi = m # m인경우 예산을 다 소진할때까지 탐색 
    hi = max(a) # max(a)인경우 부서요청지급하고 예산을 다 사용하지 않아도 됨 = 부서별 요청의 최대값이 상한액 
    
    while lo <= hi:
        mid = (lo+hi) // 2
        if check(mid): 
            lo = mid+1
            res = mid
        else: 
            hi = mid-1 

    print(res)

main()


'''
4
140 110 135 150
510

133

n :부서수 
a :부서별 요청 예상
m : 총예산 (초과하면 안됨)

res : 총예산 초과하지 않으면서 최대한 배정할수 있는값 (133 상한 = 509원, 134 상한 = 512원)

'''

