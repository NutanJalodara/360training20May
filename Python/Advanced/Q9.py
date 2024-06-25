def run_length_encode(input_str):
    if not input_str:
        return ""
    
    encoded_str = ""
    count = 1
    current_char = input_str[0]

    for char in input_str[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_str += current_char + str(count)
            count = 1
            current_char = char
    
    encoded_str += current_char + str(count)
    return encoded_str

user_input = input("Enter a string: ")
output = run_length_encode(user_input)
print(output)
