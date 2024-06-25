def get_even_length_strings_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            even_length_words = []
            for word in words:
                if len(word) % 2 == 0:
                    even_length_words.append(word)
            result = ' '.join(even_length_words)
            return result
    except FileNotFoundError:
        return "File not found."

file_path = '/Volumes/Nutan/360Training/360training20May/Python/Advanced/doc.txt'
result = get_even_length_strings_from_file(file_path)
print(result)
