
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

arr = [1, 3, 5, 7, 9, 11, 13]
target = 3

result = binary_search(arr, target)

if result != False:
    print(f"Element found at index {result}")
else:
    print("Element not found")
