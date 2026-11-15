import csv
import time

# Load product IDs from the cleaned CSV file
product_ids = []

with open("TIMA_Retail_Cleaned.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product_ids.append(row["product_id"])


def sequential_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Prepare sorted data for binary search
sorted_product_ids = sorted(product_ids)

target = product_ids[7]
iterations = 10000

# Measure sequential search
start = time.perf_counter()

for _ in range(iterations):
    sequential_result = sequential_search(product_ids, target)

sequential_total = time.perf_counter() - start
sequential_average = (sequential_total / iterations) * 1_000_000

# Measure binary search
start = time.perf_counter()

for _ in range(iterations):
    binary_result = binary_search(sorted_product_ids, target)

binary_total = time.perf_counter() - start
binary_average = (binary_total / iterations) * 1_000_000

# Display results
print("TIMA RETAIL STORE - SEARCH RESULTS")
print("----------------------------------")
print("Total records:", len(product_ids))
print("Target Product ID:", target)
print("Sequential Search Position:", sequential_result)
print("Binary Search Position:", binary_result)
print("Number of Test Iterations:", iterations)
print(f"Sequential Average Time: {sequential_average:.6f} microseconds")
print(f"Binary Average Time: {binary_average:.6f} microseconds")