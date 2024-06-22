def get_unique_elements(input_list):
    unique_elements = []
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

list1 = [1, 2, 2, 3, 4, 4, 5, 5]
print(get_unique_elements(list1))