import time

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


arr = list(range(1, 100001))

# Best Case
start = time.perf_counter()
linear_search(arr, 1)
end = time.perf_counter()
print("Best Case Time:", end - start, "seconds")

# Average Case
start = time.perf_counter()
linear_search(arr, 50000)
end = time.perf_counter()
print("Average Case Time:", end - start, "seconds")

# Worst Case
start = time.perf_counter()
linear_search(arr, 100000)
end = time.perf_counter()
print("Worst Case Time:", end - start, "seconds")