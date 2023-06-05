# 접근) 

def main():
    N = int(input())
    a = list(map(int,input().split()))
    x = int(input())
    a.sort() # 오름차순 정렬
    left = 0
    right = N - 1
    res = 0
    while left < right:
        sum = a[left] + a[right] # 현재 가리키고 있는 값들 더하기    
        if sum == x: # 더한 값이 x와 같은 경우 카운팅 하고 포인터 둘 다 이동
            res += 1
            left += 1
            right -= 1
        elif sum < x: # 더한 값이 x보다 작은 경우 왼쪽 포인터만 이동
            left += 1
        else: # 더한 값이 x보다 큰 경우 오른쪽 포인터만 이동
            right -= 1
    print(res)

if __name__ == "__main__":
    main()

'''
9
5 12 7 10 9 1 2 3 11
13

3

문제
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다.(1 <= ai <= 1,000,000)
자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의수

입력
n : 수열의 크기
a : 수열에 포함되는 수 
x : 합의 기준수 (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

출력
문제의 조건을 만족하는 쌍의 개수를 출력한다.

'''