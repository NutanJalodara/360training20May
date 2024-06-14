user_input = input("Enter a string: ")
letters = 0
digits = 0  
for char in user_input:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
print(f"Alphabets: {letters} & Number: {digits}")