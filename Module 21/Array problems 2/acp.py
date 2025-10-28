
a = [4, 5, 234, 2, 6, 82, 234, 5234]

min_val = a[0]
max_val = a[0]

for i in range(1, len(a)):
    if a[i] < min_val:
        min_val = a[i]
    elif a[i] > max_val:
        max_val = a[i]

max_diff = max_val - min_val

print("Maximum difference: ", max_diff)
