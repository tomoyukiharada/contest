#AtCoder Beginner Contest 136 B - Uneven Numbers
N = int(input())
count = 0
if (10 <= N):
  count += 9
  if (100 <= N):
    if (1000 <= N):
      count += (9 * 10 * 10)
      if (10000 <= N):
        count += (N - 10000 + 1)
        if (100000 == N):
          count -= 1
    else:
      count += (N - 100 + 1)
else:
  count += N
print(count)