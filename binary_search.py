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


arr = list(range(1, 100001))

# Best Case
start = time.perf_counter()
binary_search(arr, 50000)
end = time.perf_counter()
print("Best Case Time:", end - start, "seconds")

# Average Case
start = time.perf_counter()
binary_search(arr, 25000)
end = time.perf_counter()
print("Average Case Time:", end - start, "seconds")

# Worst Case
start = time.perf_counter()
binary_search(arr, 100001)
end = time.perf_counter()
print("Worst Case Time:", end - start, "seconds")