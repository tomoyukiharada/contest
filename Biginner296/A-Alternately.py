#A - Alternately
N = int(input())
S = input()
stack = S[0]
flg = True
for i in range(1,N):
  sex = S[i]
  if (stack == sex):
    print("No")
    flg = False
    break
  else:
    stack = S[i]
    continue
if flg:
  print("Yes")
