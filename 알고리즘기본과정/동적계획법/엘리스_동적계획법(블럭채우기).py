# 접근) n == 1, 0,1, 디버깅) if n == 1 return 1

def fillBox(n):
    if n == 1:
        return 1 
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def main():
    n = int(input())
    print(fillBox(n))

if __name__ == "__main__":
    main()

'''
4

5
상자를 블럭으로 채우는 경우의 수를 1,000,000,007로 나눈 나머지를 출력합니다.
'''