# 완전탐색(i&j)_4.덩치(백준)

n = int(input())
a = []

def main():
    for i in range(n): 
        x,y = map(int,input().split())
        a.append((x,y))

    for i in a: 
        x,y = i 
        rank = 1
        for j in a:
            p,q = j
            if x < p and y < q:
                rank+=1
        print(rank, end=' ')

if __name__ == "__main__":
    main()

'''
문제) 덩치(x, y) : 몸무게 x, 키 y
측정자 (x, y), 대상자 (p, q), x > p and y > q일 경우에만 덩치가 더 크다
덩치가 제일 큰 경우 1등, 그다음 덩치는 k+1등 (등수는 동률가능)

이름(몸무게, 키)	덩치 등수
A	(55, 185)	2
B	(58, 183)	2
C	(88, 186)	1
D	(60, 175)	2
E	(46, 155)	5

입력
n = 전체사람수 
(x,y) = 각 사람의 몸무게/키 

출력
덩치등수구해서 한줄에 표시 (공백 표기)

제한
2 ≤ N ≤ 50
10 ≤ x, y ≤ 200

문제)
5
55 185
58 183
88 186
60 175
46 155

2 2 1 2 5
'''