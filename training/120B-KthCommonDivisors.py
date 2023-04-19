#AtCoder Beginner Contest 120 B - K-th Common Divisors
A, B, K = map(int, input().split())
count = 0
n = min(A, B)
while (1 < n):
  if ((A % n == 0) & (B % n == 0)):
    count += 1
    if (count == K):
      break
  n -= 1
print(n)