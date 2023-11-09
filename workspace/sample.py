N = int(input())
A = list(map(int, input().split()))

MAX = max(A)
Leng = 2*N+2

first = "+" + "-"*(Leng-1)
print(first)

# i行目の出力
for i in range(MAX+2):
  i = i+1
  s = ""
  for j in range(Leng):
    j = j+1
    # 1文字目
    if j == 1:
      s += "|"
    elif j % 2 == 0:
      s += "."
    else:
      p = (j-1)//2
      if i <= A[p-1]:
        s += "X"
      elif i == A[p-1] + 1:
        s += "V"
      else:
        s += "."
  if i != 1:
    print(s)

print(first)