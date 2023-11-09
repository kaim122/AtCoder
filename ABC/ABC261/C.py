N = int(input())

S = {}

for _ in range(N):
    s = input()
    S[s] = S.get(s,-1) + 1
    if S[s]:
        print(f'{s}({S[s]})')
    else:
        print(s)