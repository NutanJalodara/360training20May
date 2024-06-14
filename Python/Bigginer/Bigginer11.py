number = int(input("Enter a number: "))
def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits = sum_digits + (n % 10)
        n = n // 10
    return sum_digits

while number >= 10:
    number = sum_of_digits(number)

print("The single-digit sum is:", number)
