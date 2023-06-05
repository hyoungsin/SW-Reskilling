'''
접근) n,a,left/right_heap,heappush,heappush,left_heap[0] (5)  or, while not , =left_heap[0]
'''
from heapq import *
def main():
    n= int(input())
    a = list(map(int, input().split()))
    left_heap = []
    right_heap = []

    for i in a:
        if len(left_heap) == 0 or len(right_heap) == 0: 
            heappush(left_heap,-i)
        elif i < -left_heap[0]: 
            heappush(left_heap,-i)
        else:
            heappush(right_heap,i)
        
        while not (len(left_heap) == len(right_heap) or len(left_heap) == len(right_heap)+1):
            if len(left_heap) < len(right_heap):
                heappush(left_heap,-heappop(right_heap))
            else:
                heappush(right_heap,-heappop(left_heap))

        print(-left_heap[0],end=' ')

if __name__ == "__main__":
    main()


'''

8
1 8 6 5 1 1 2 6

1 1 6 5 5 1 2 2

엘리스는 가만히 있으면 중간은 간다라는 속담을 좋아합니다. 하지만 스펙 경쟁이 과열된 현대 사회에서 중간이라도 가기란 쉽지 않은 일이 되어버렸습니다.
지금 이 순간에도 엘리스가 있는 방에는 성적이 i인 카드 병정들이 들어오고 있습니다. 중간을 좋아하는 엘리스를 위해 성적이 중간인 카드 병정의 성적을 구해주세요!
i명의 카드 병정의 성적이 A1,A2... An까지 주어질때 성적이 중간인 카드 병정의 성적은 성적을 오름차순으로 정렬했을 때  (i+1)/2번째 성적을 의미함
이때 ⌊x⌋는 x보다 작거나 같은 가장 큰 정수를 의미합니다.
1≤N≤100,000
1≤A≤100,000
'''