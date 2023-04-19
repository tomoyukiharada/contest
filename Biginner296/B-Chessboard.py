#B - Chessboard
S = []
J = ["a","b","c","d","e","f","g","h",]
I = ["8","7","6","5","4","3","2","1",]
for i in range(8):
  s = input()
  S.append(s)
for i in range(8):
  for j in range(8):
    if (S[i][j] == "*"):
      s = J[j] + I[i]
      print(s)