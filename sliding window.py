n = int(input())
k = int(input())
num = list(map(int, input().split()))
sum = 0
max = 0
for i in range(k):
    sum =sum + num[k+i] - num[i]
    if sum >max:
         max = sum
print(max)    