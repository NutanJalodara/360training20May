def rotate_array_right(arr, D):
    N = len(arr)
    D = D % N
    rotated_arr = arr[-D:] + arr[:-D]
    return rotated_arr

arr = [1, 2, 3, 4, 5]
D = 2
rotated_arr = rotate_array_right(arr, D)
print(f"Array after rotation: {rotated_arr}")
