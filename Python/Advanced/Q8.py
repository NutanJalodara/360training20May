def parse_encoded_string(encoded_str):
    parts = encoded_str.split('0')
    filtered_parts = list(filter(None, parts))
    first_name = filtered_parts[0]
    last_name = filtered_parts[1]
    id_value = filtered_parts[2]
    result = {
        "first_name": first_name,
        "last_name": last_name,
        "id": id_value
    }
    return result

user_input = input("Enter a string: ")
output = parse_encoded_string(user_input)
print(output)
