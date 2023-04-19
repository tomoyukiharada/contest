#AtCoder Beginner Contest 057 C - Digits in Multiplication
N = int(input())
import math
divisores = []
n = 1
while (n <= int(math.sqrt(N))):
  if (N % n == 0):
    divisores.append(max(int(math.log10(int(n))+1),int(math.log10(int(N/n))+1)))
  n += 1
print(min(divisores))