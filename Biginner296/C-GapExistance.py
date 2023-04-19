#C - Gap Existence
N, X = map(int, input().split())
A = [int(i) for i in input().split()]
flg = True
for i in range(N):
  for j in range(i,N):
    if ((A[i] - A[j]) == X):
      print("Yes")
      flg= False
      break
  if not flg:
    break
if flg:
  print("No")