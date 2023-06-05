# 접근) n,m,a,left,s,right

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    left = a[:m-1]
    s = a[m-1]
    right = a[m:]
    sum = 0 
    for i in left:
        sum += min(i,s)
    for i in right:
        sum += min(i,s-1)
    print(sum+s)


if __name__ == '__main__':
    main()


'''
티켓 구매
N명의 사람이 일렬로 줄을 서서 티켓을 구매하고 있습니다. 앞에서 i번째 사람이 사려고 하는 티켓은 
t개입니다.

줄의 맨 앞의 사람은 티켓 1장을 살 수 있습니다. 티켓의 구매에는 1초가 소요됩니다. 
아직 사야 할 티켓이 남은 사람은 티켓을 산 뒤에 다시 줄의 맨 뒤로 가서 줄을 섭니다.

앞에서 K번째 사람이 필요한 모든 티켓을 사는 데 걸리는 시간을 구해주세요.

5 4
2 4 1 3 2

11
'''