start = 1
stop = 10
odd_sum = 0
for num in range(start, stop + 1):
    if num % 2 != 0:
        odd_sum += num
print(f"Sum of odd numbers between {start} and {stop}: {odd_sum}")
