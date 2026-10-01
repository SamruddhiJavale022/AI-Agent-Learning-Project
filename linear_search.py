import time

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Create array with 100000 elements
arr = list(range(1, 100001))

# Best Case (element at first position)
start = time.perf_counter()
result = linear_search(arr, 1)
end = time.perf_counter()
print("Best Case:")
print("Index =", result)
print("Execution Time =", end - start, "seconds\n")

# Average Case (element in middle)
start = time.perf_counter()
result = linear_search(arr, 50000)
end = time.perf_counter()
print("Average Case:")
print("Index =", result)
print("Execution Time =", end - start, "seconds\n")

# Worst Case (element at last position)
start = time.perf_counter()
result = linear_search(arr, 100000)
end = time.perf_counter()
print("Worst Case:")
print("Index =", result)
print("Execution Time =", end - start, "seconds")