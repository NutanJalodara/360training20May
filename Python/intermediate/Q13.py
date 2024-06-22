starts_with = lambda string, char: string.startswith(char)

input_string = input("Enter the string: ")
input_char = input("Enter the starting character to check: ")
result = starts_with(input_string, input_char)
if result:
    print(f"The string '{input_string}' starts with the character '{input_char}'.")
else:
    print(f"The string '{input_string}' does not start with the character '{input_char}'.")
