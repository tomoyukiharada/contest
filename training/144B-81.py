#AtCoder Beginner Contest 144 B - 81
N = int(input())
product = []
flg = True
for i in range(1,10):
  for j in range(1,10):
    product.append(int(i*j))
#print(product)
for num in product:
  if (num == N):
    print("Yes")
    flg = False
    break
if flg:
  print("No")