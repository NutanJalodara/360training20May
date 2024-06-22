def is_power_of_two(n):
    if n == 1:
        return True
    if n < 1 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

num = int(input("Enter a number: "))

if is_power_of_two(num):
    print(f"{num} is a power of two.")
else:
    print(f"{num} is not a power of two.")
