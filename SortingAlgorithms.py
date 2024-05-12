import random
import timeit

def nearly_sorted_dataset(n):
    nums = list(range(1, n + 1))
    for i in range(int(0.1 * n)):
        idx1 = random.randint(0, n - 1)
        idx2 = random.randint(0, n - 1)
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
    return nums

def reversed_dataset(n):
    return list(range(n, 0, -1))

def random_dataset(n):
    return [random.randint(1, n) for _ in range(n)]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def counting_sort(arr):
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    for num in arr:
        counts[num] += 1
    sorted_arr = []
    for i in range(len(counts)):
        sorted_arr.extend([i] * counts[i])
    return sorted_arr

def shaker_sort(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
    return arr

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10
    return arr

def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

# Test the algorithms
algorithms = {
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Counting Sort": counting_sort,
    "Shaker Sort": shaker_sort,
    "Radix Sort": radix_sort
}

datasets = {
    "Nearly Sorted": nearly_sorted_dataset,
    "Random": random_dataset,
    "Reversed": reversed_dataset
}

n = 100000
for dataset_name, dataset_func in datasets.items():
    dataset = dataset_func(n)
    print(f"\nDataset: {dataset_name}")
    for alg_name, alg_func in algorithms.items():
        time_taken = timeit.timeit(lambda: alg_func(dataset.copy()), number=1)
        print(f"{alg_name}: {time_taken:.6f} seconds")
