#접근 : n,m,a,Q, Q[val]

from collections import deque
def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    Q = [deque()for i in range(1,10)]
    res = 0 

    for i in range(n): 
        val = a[i]
        while len(Q[val]) > 0 and i - Q[val][0] > m:
            Q[val].popleft()

        res += len(Q[val])
        Q[val].append(i)
    print(res)


if __name__ == "__main__":
    main()


'''

6 2
1 1 1 2 1 2

5

1부터 9까지 숫자가 쓰여있는 카드 
N장이 일렬로 나열되어있습니다. i번째 카드에는 A가 쓰여있습니다.

Ai =Aj
i<j
0 < j-i <=K
A1 ... An K가 주어질 때, 친한 카드 쌍의 개수를 구해주세요!

1≤K<N≤100,000
1≤A≤9
'''