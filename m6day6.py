# 🔹 DAY 6 - SORTING


# 🔹 1. Bubble Sort

def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# 🔹 2. Selection Sort

def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:

                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# 🔹 3. Insertion Sort

def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr


# 🔹 4. Sort Strings Alphabetically

def sort_strings(words):

    return sorted(words)


# 🔹 5. Sort Dictionary by Values

def sort_dict_by_values(data):

    return dict(
        sorted(data.items(),
               key=lambda item: item[1])
    )


# 🔹 MAIN PROGRAM

numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original Array:")
print(numbers)


print("\n🔹 Bubble Sort")
print(bubble_sort(numbers.copy()))


print("\n🔹 Selection Sort")
print(selection_sort(numbers.copy()))


print("\n🔹 Insertion Sort")
print(insertion_sort(numbers.copy()))


print("\n🔹 Sort Strings Alphabetically")

words = ["python", "java", "c", "javascript"]

print(sort_strings(words))


print("\n🔹 Sort Dictionary by Values")

student_marks = {
    "Rahul": 85,
    "Vikyat": 92,
    "Anil": 78,
    "Kiran": 88
}

print(sort_dict_by_values(student_marks))