n = int(input())
S = input()
if S == "BA" or (S[0] == "A" and S[-1] == "B"):
    print("No")
else:
    print("Yes")