L1,R1,L2,R2 = map(int,input().split())

ans = 0
for i in range(101):
    if L1 <= i and i <= R1 and L2 <= i and i <= R2:
        ans += 1

if ans == 0:
    print(ans)
else:
    print(ans-1)

# ans = max(0,min(R1,R2)-max(L1,L2)) が最もシンプル