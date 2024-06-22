def find_median(number_list):
    sorted_list = sorted(number_list)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2.0
    else:
        median = sorted_list[mid]
    return median

number_list = [7, 2, 5, 1, 9, 3]
median = find_median(number_list)
print(f"Median: {median}")
