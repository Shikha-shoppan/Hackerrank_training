def count_unique_pairs_with_diff(arr, k):
    unique_values = set(arr)

    if k == 0:
        from collections import Counter
        freq = Counter(arr)
        return sum(1 for count in freq.values() if count > 1)

    count = 0
    for val in unique_values:
        if val + k in unique_values:
            count += 1
    return count

n = int(input())
arr = list(map(int, input().split()))
k = int(input())


print(count_unique_pairs_with_diff(arr, k))
