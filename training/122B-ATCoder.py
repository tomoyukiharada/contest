#AtCoder Beginner Contest 122 B - ATCoder
#問題設定
S = input()
target = ["A","C","G","T"]
#変数定義
index = 0
longest = 0
longest_prelim = 0
#function
def isTarget(S, target, index):
  flg = True
  for char in target:
    if (S[index] == char):
      flg = False
      return True
  if flg:
    return False
#main
while (index < len(S)):
  if (isTarget(S, target, index)):
    index += 1
    longest_prelim += 1
    if (longest < longest_prelim):
      longest = longest_prelim
  else:
    index += 1
    longest_prelim = 0
print(longest)