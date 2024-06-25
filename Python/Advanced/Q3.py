def JtoI(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        corrected_content = content.replace('J', 'I')
        print(corrected_content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

file_path = '/Volumes/Nutan/360Training/360training20May/Python/Advanced/WORDS.TXT'
JtoI(file_path)