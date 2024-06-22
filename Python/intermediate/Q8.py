def count_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

inputString = input("Enter a string: ")
vowel_count = count_vowels(inputString)
print(f"Number of vowels: {vowel_count}")
