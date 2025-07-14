# Read input
prices = list(map(int, input().strip().split(',')))

total_profit = 0

for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        total_profit += prices[i] - prices[i - 1]

print(total_profit)
