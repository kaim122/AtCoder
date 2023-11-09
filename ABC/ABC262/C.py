N = int(input())
a = list(map(int, input().split()))

for i in range(N):
    a[i] -= 1

ans = 0
cnt1 = 0
for i in range(N):
    if a[i] == i:
        cnt1 += 1

ans += cnt1*(cnt1-1)//2
cnt2 = 0
for i in range(N):
    j = a[i]
    if i < j and a[j] == i:
        cnt2 += 1
ans += cnt2

print(ans)