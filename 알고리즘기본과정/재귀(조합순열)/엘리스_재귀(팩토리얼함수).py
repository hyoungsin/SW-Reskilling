# fatorial 산출함수 작성 (재귀개념 활용)

def fac(n): 
    if n == 0: #기저조거 
        return 1
    return n*fac(n-1)

print(fac(4))