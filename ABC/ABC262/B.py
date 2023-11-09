N,M = map(int, input().split())
G = [[False] * N for _ in range(N)]

for i in range(M):
    u,v = map(int, input().split())
    G[u-1][v-1] = True
    G[v-1][u-1] = True

cnt = 0
for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            if G[a][b] and G[b][c] and G[c][a]:
                cnt += 1

print(cnt)