#AtCoder Beginner Contest 095 C - Half and Half
A,B,C,X,Y = map(int, input().split())
import math
price_min = math.inf
for numAB in range(0, max(X,Y)*2+1):
  if (0 <= X-int(numAB/2)):
    numA = X-int(numAB/2)
  else:
    numA = 0
  if (0 <= Y-int(numAB/2)):
    numB = Y-int(numAB/2)
  else:
    numB = 0
  price = numA*A + numB*B + numAB*C
  if (price < price_min):
    price_min = price
print(price_min)