N,A,B = map(int, input().split())

# 周期回数 × nmodA < Bを満たす個数　＋　最終周期の個数
def f(x):
    return x//A * min(A,B) + min(x % A, B-1); 

if A > N:
    print(0)
else:
    print(f(N)-f(A-1))