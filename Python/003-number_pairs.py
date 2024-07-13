# In this kata the aim is to compare each pair of integers from 
# two arrays, and return a new array of large numbers.
# Note: Both arrays have the same dimensions.

def get_larger_numbers(a: list, b: list) -> list:
    new_arr: list = []
    for i in range(len(a)):
        new_arr.append(max(a[i], b[i]))
    return new_arr


if __name__ == '__main__':
    arr1: list = [13, 64, 15, 17, 88]
    arr2: list = [23, 14, 53, 17, 80]
    print(get_larger_numbers(arr1, arr2)) # [23, 64, 53, 17, 88]
