import time

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Create array with 100000 elements
arr = list(range(1, 100001))

# Best Case (middle element)
start = time.perf_counter()
result = binary_search(arr, 50000)
end = time.perf_counter()
print("Best Case:")
print("Index =", result)
print("Execution Time =", end - start, "seconds\n")

# Average Case
start = time.perf_counter()
result = binary_search(arr, 25000)
end = time.perf_counter()
print("Average Case:")
print("Index =", result)
print("Execution Time =", end - start, "seconds\n")

# Worst Case (element not present)
start = time.perf_counter()
result = binary_search(arr, 100001)
end = time.perf_counter()
print("Worst Case:")
print("Index =", result)
print("Execution Time =", end - start, "seconds")