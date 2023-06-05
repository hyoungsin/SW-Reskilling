
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def val(mid):
    global n,m,a,res # m : 파개수 
    sum = 0 
    for i in a: 

        if mid > i: # 한개 파라도 사용하지 않으면 중단 
            continue

        # print('i,mid:',i,mid)

        sum += i//mid # 그외는 sum에 추가시킴 

        # print('sum',sum)

    return sum >= m # m과 같은경우에만 true반환 

def main():
    global n,m,a,res 
    n,m = map(int,read().rstrip().split())

    # print(n,m)

    a = []
    for i in range(n): 
        a.append(int(read().rstrip()))

    lo = 1 # 제일 적은 파 단위와 가장 큰 파단위 (0입력하면 divison error)
    hi = max(a)

    # print('low,hi:',lo,hi)

    res = 0
    while lo <= hi: # 최솟값과 최댓값이 만나면 중단 (등호가 없으면 최소 최대값이 답일 경우 틀림,중간부터 탐색하기때문)
        mid = (lo+hi) // 2 # 중간값 (답)

        # print('mid:',mid)

        if val(mid): # 중간값이라면 파의 갯수를 만족하는 대상, 최솟값 만드려면 계속 올려야함 
            lo = mid+1 # min값을 1씩 증가 
            res = mid # 만족하는 숫자의 최종 mid값 (위에서 fail하면 if문 타지 않음 

        else:
            hi = mid-1 # sum이 만족스럽지 못할 경우 높이를 낮춤 (fail하면 mid는 update되지 않음)
    
    print(sum(a)-res*m) #전체 파의 길이 에서 res * 파의 개수

main()

'''
3 5
440
350
230

145

파닭 하나당 넣을 수 있는 최대 파의 길이는 175cm으로, 
440cm 파에서 2개, 350cm 파에서 2개, 230cm 파에서 1개, 총 5개의 파닭을 만들 수 있고, 
각각의 파에서 90cm + 0cm + 55cm = 145cm의 파가 남는다.

승균이는 가게를 오픈하기 전에 남부시장에 들러서 길이가 일정하지 않은 파를 여러 개 구매하였다. 
승균이는 같은 양의 파를 넣는다. 
파의 양을 최대한 많이 넣으려고 한다.(하지만 하나의 파닭에는 하나 이상의 파가 들어가면 안 된다.) 
라면에 넣을 파의 양을 구하는 프로그램을 작성하시오. 
승균이네 치킨집 자는 정수만 표현되기 때문에 정수의 크기로만 자를 수 있다.

입력
첫째 줄에 승균이가 시장에서 사 온 파의 개수 S(1 ≤ S ≤ 1,000,000), 
그리고 주문받은 파닭의 수 C(1 ≤ C ≤ 1,000,000)가 입력된다. 
파의 개수는 항상 파닭의 수를 넘지 않는다. (S ≤ C) 그 후, S 줄에 걸쳐 파의 길이 L(1 ≤ L ≤ 1,000,000,000)이 정수로 입력된다.

출력
승균이가 라면에 넣을 파의 양을 출력한다.'''