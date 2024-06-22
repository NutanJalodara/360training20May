def count_pairs_with_sum(arr, K):
    counts = {}
    pair_count = 0
    for num in arr:
        complement = K - num
        if complement in counts:
            pair_count += counts[complement]
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return pair_count

arr = [1, 2, 3, 4, 5]
k = 6
pair_count = count_pairs_with_sum(arr, k)
print(f"Pair count: {pair_count}")
