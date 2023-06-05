# 이진탐색 (bisect활용)

import sys
from bisect import *
read = sys.stdin.readline

def main():
    N, H = map(int, read().rstrip().split())
    down = []
    up = []
    for i in range(N):
        if i % 2 == 0:
            down.append(int(read().rstrip()))
        else:
            up.append(int(read().rstrip()))

    # 최솟값 구하는 문제
    res = int(1e9)
    cnt = 0
    down.sort()
    up.sort()
    # 높이 1부터 H까지 다 해보기
    for i in range(1, H + 1):
        # left는 값을 왼쪽으로 반환 하므로 반환값부터 끝까지 다 만나는 장애물임. 개수는 N // 2 - down_cnt
        down_cnt = bisect_left(down, i)
        # right는 값을 오른쪽으로 반환 하므로 H - i 를 탐색하면 같은 값 오른쪽을 반환해줌. 반환값부터 끝까지 다 만나는 장애물임. 개수는 N // 2 - up_cnt
        up_cnt = bisect_right(up, H - i)
        # 파괴 하는 장애물 개수
        sum = N - down_cnt - up_cnt

        # 최솟값 갱신 되는 경우
        if sum < res:
            res = sum
            cnt = 1

        # 최솟값과 같은 경우
        elif sum == res:
            cnt += 1

    print(res,cnt)

main()


'''
6 7
1
5
3
3
5
1

2 3

n : 종유석/석순의 개수 (짝수)
m : 동굴의 높이 (첫 번째 장애물은 항상 석순이고, 그 다음에는 종유석과 석순이 번갈아가면서 등장한다.)
일직선으로 지나가면서 만나는 모든 장애물을 파괴한다.
위의 그림에서 4번째 구간으로 개똥벌레가 날아간다면 파괴해야하는 장애물의 수는 총 여덟개이다. 
(4번째 구간은 길이가 3인 석순과 길이가 4인 석순의 중간지점을 말한다)
하지만, 첫 번째 구간이나 다섯 번째 구간으로 날아간다면 개똥벌레는 장애물 일곱개만 파괴하면 된다.
동굴의 크기와 높이, 모든 장애물의 크기가 주어진다. 
이때, 개똥벌레가 파괴해야하는 장애물의 최솟값과 그러한 구간이 총 몇 개 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 H가 주어진다. N은 항상 짝수이다. (2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000)
다음 N개 줄에는 장애물의 크기가 순서대로 주어진다. 장애물의 크기는 H보다 작은 양수이다.

출력
첫째 줄에 개똥벌레가 파괴해야 하는 장애물의 최솟값과 그러한 구간의 수를 공백으로 구분하여 출력한다.
'''