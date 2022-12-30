"""
Selection Sort
"""
num = [2, 3, 1]

def selection_sort(arr):
    """_summary_

    Args:
        arr (_type_): _description_
    """
    for x in range(0, len(arr) - 1):
        min = x
        for y in range(1, len(arr)):
            if arr[min] > arr[y]:
                min = y
        temp = arr[x]
        arr[x] = arr[min]
        arr[min] = temp

selection_sort(num)
print(num)
  