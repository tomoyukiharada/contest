#AtCoder Beginner Contest 128 C - Switches
#input
N, M = map(int, input().split())
balbs = []
for i in range(M):
  balb = [int(i) for i in input().split()]
  balbs.append(balb)
p = map(int, input())
#main
import math
count = 0
for s in range(0, math.comb(2,N)): #for all switches
  for b in range(0, M): #for all balbs
    if (sum % 2) == p:
      count += 1
print(count)
#check
print(N, M)
for i in range(len(balbs)):
  print(balbs[i])
print(p)