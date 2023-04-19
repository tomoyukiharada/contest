#AtCoder Beginner Contest 106 B - 105
N = int(input())
count = 0
n = 1
def handler(n):
  m = 1
  num = 0
  while (m <= n):
    if (n % m == 0):
      num += 1
    m += 1
  if (num == 8):
    return True
  else:
    return False
while (n <= N):
  if handler(n):
    count += 1
  n += 2
print(count)