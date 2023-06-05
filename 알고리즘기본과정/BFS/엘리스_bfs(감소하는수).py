# 접근 : Q, 시작조건, 나머지로 인덱스 조절, n까지만 (n+1) 추출

from collections import deque
def main():
    n = int(input())
    Q = deque([1,2,3,4,5,6,7,8,9]) # 문제에서 주어진 조건 (기저조건 : 이숫자에서 시작함)
    res = [i for i in range(10)] # 결과값 리스트도 미리 주어짐 이기준에서 append함 

    if n <10: # 만약 입력숫자가 10보다 적으면 사전에 알고 있는 값으로 출력 
        print(res[n])
        return

    while len(Q) > 0 :  # append가 더이상 안될때까지 (예) 9876543210 이후에는 없음 index는 계속 줄어듬 
        if len(res) >= n+1: # 결과값이 n+1이상이 출력되더라도 의미 없음 break (예 : n =18만 반환 n=19 안궁금)
            break
        x = Q.popleft() #  x를 pop 해서 10을 곱하고 적은수를 더하는 구조로 만듬 pop은 x를 희생해서 res를 채워나가는 과정 
        for i in range(x%10): # 단 range는 더 적은수만 와야 하므로 나머지연산을 응용함 (예) 3%10  = 0,1,2만 올수 있음 
            Q.append(x*10+i) # 내림수 조건에 맞으면 Q에저장해서 다음수를 산출하기 위한 준비를 해야함 
            res.append(x*10+i) # 내림수 조건에 맞는수는 결과리스트에 저장해야함 
    
    if len(res) < n+1: # 만약 결과치가 n+1 (0포함) 보다 적으면 (예) n = 8 인데 len 8 (0~7) 이면 8이 없다는 의미)
        print(-1) # 값이 없으므로 -1 출력 
    else:
        print(res[n]) # 그렇지 않다면 산출값을 출력 

main()

'''
18

42
'''