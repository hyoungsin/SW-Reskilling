
# 접근 : (rotate함수,원본배열(a),rotate배열(k) (1) 입력값 주의 

def rotate(a, k):
    left = a[-k:] # 배열 회전 공식
    right = a[:-k]
    return left + right

def main():
    n, m = map(int, input().split())
    a = list(map(int,input().split()))
    for i in range(m): #3번 회전 
        x = list(map(int,input().split()))
        if x[0] == 1:
            a.reverse() #1로 시작하면 reverse 함수 적용
        else:
            a = rotate(a, x[1]) #2로 시작하면 rotate함수 적용
    for i in a:
        print(i, end = ' ') # 옆으로 공백 print 

if __name__=="__main__":
    main()

'''
A에 다음의 연산을 Q번 적용하려고 합니다.
1: 배열을 좌우 반전시킵니다
(1,2,3,4,5,6)→(6,5,4,3,2,1)

2 k“: 배열을 k칸 오른쪽으로 회전시킵니다
(1,2,3,4,5,6)→(3,4,5,6,1,2)if k=4
(3,4,5,6,1,2)→(2,3,4,5,6,1)if k=1
연산을 차례대로 모두 적용한 뒤 배열의 상태를 출력해주세요!

연산을 차례대로 모두 적용한 뒤 배열의 상태를 출력해주세요!

6 3
1 2 3 4 5 6
2 4
2 1
1

1 6 5 4 3 2

'''