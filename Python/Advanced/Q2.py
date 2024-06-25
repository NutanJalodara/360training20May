def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
        return line_count
    except FileNotFoundError:
        return f"File '{file_path}' not found."

file_path = '/Volumes/Nutan/360Training/360training20May/Python/Advanced/demo.txt'
print(count_lines_in_file(file_path))