A = [99, 12, 74, 56, 87, 24]
for i in range(len(A)):
    min_index = i
    for j in range(i + 1, len(A)):
        if A[min_index] > A[j]:
            min_index = j
    A[i], A[min_index] = A[min_index], A[i]
print("Sorted array")
print(A)