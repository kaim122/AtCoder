N = int(input())

ans = N

if N % 4 == 0:
    ans += 2
elif N % 4 == 1:
    ans += 1
elif N % 4 == 3:
    ans += 3

print(ans)