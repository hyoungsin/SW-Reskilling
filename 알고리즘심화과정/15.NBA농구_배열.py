# https://www.acmicpc.net/problem/2852

n = int(input())
a = []
for i in range(n):
    team,time = input().split()
    m,s = time.split(':')
    team,m,s = map(int,(team,m,s))
    s = m*60 + s 
    a.append([team,s])

a = a + [[0,48*60]]

print (a)

t1 = 0
t2 = 0 
t1_s  = 0
t2_s = 0 
res = []
for i in range(n):

    # print(a[i][0])
    
    if a[i][0] == 1:# t1 이긴회쉬
        t1+=1

    elif a[i][0] == 2: # t2 이긴회쉬
        t2+=1

    # print(t1,t2)

    if t1 > t2: 
        t1_s += a[i+1][1] - a[i][1] 

        # print(t1_s)

        t1_m = t1_s // 60 
        t1_s = '{:02d}'.format(t1_s % 60)

        # print(t1_m,t1_s)

        res.append('{}:{}'.format(t1_m,t1_s))



    if t2 > t1: 
        t2_s += a[i+1][1] - a[i][1] 

        # print(t2_s)


        t2_m = t2_s // 60 
        t2_s = '{:02d}'.format(t2_s % 60)

        # print(t2_m,t2_s)

        res.append('{}:{}'.format(t2_m,t2_s))

for i in res:
    print(i)


'''
3
1 01:10
2 21:10
2 31:30

20:00
16:30

문제
동혁이는 NBA 농구 경기를 즐겨 본다. 동혁이는 골이 들어갈 때 마다 골이 들어간 시간과 팀을 적는 이상한 취미를 가지고 있다.

농구 경기는 정확히 48분동안 진행된다. 각 팀이 몇 분동안 이기고 있었는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 골이 들어간 횟수 N(1<=N<=100)이 주어진다. 둘째 줄부터 N개의 줄에 득점 정보가 주어진다. 득점 정보는 득점한 팀의 번호와 득점한 시간으로 이루어져 있다. 팀 번호는 1 또는 2이다. 득점한 시간은 MM:SS(분:초) 형식이며, 분과 초가 한자리 일 경우 첫째자리가 0이다. 분은 0보다 크거나 같고, 47보다 작거나 같으며, 초는 0보다 크거나 같고, 59보다 작거나 같다. 득점 시간이 겹치는 경우는 없다.

출력
첫째 줄에 1번 팀이 이기고 있던 시간, 둘째 줄에 2번 팀이 이기고 있던 시간을 출력한다. 시간은 입력과 같은 형식(MM:SS)으로 출력한다.
'''

