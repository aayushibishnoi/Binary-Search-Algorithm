def is_sorted(arr):
    """Check if the array is sorted in ascending order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def binary_search_iterative(arr, target):
    """Iterative binary search: Returns index of target or -1 if not found."""
    if not is_sorted(arr):
        raise ValueError("Array must be sorted")
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(arr, target, left, right):
    """Recursive binary search: Returns index of target or -1 if not found."""
    if not is_sorted(arr):
        raise ValueError("Array must be sorted")
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

def main():
    # Sample sorted array
    arr = [2, 3, 4, 10, 40, 50, 60, 70]
    print(f"Array: {arr}")
    
    # Test cases
    targets = [10, 3, 99]
    
    print("\n=== Iterative Binary Search ===")
    for target in targets:
        result = binary_search_iterative(arr, target)
        if result != -1:
            print(f"Element {target} found at index {result}")
        else:
            print(f"Element {target} not found in array")
    
    print("\n=== Recursive Binary Search ===")
    for target in targets:
        result = binary_search_recursive(arr, target, 0, len(arr) - 1)
        if result != -1:
            print(f"Element {target} found at index {result}")
        else:
            print(f"Element {target} not found in array")

if __name__ == "__main__":
    main()
