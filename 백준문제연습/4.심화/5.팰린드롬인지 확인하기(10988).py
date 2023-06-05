# 심화

# 전체 비교 

a1 = list(input())
a2= a1[::-1]

if a1 == a2:
    print(1)
else : print(0)


# 원소 확인

# a1 = list(input())
# n = len(a1)
# b = reversed(a1)
# a2 = []

# for i in b:
#     a2.append(i)

# cnt = 0
# for i in range(n):
#     if a1[i] == a2[i] :
#         cnt+=1

# if cnt == n : 
#     print(1)
# else: print(0)


'''
level
abcde
1

문제
알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 

level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

입력
첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.
'''