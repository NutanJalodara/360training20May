def access_list_element(lst, index):
    try:
        element = lst[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print(f"Error: Index {index} is out of range for the list.")

my_list = [10, 20, 30, 40, 50]
index_to_access = int(input("Enter an index to access: "))
access_list_element(my_list, index_to_access)
