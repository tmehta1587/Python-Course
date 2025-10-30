
arr = [0, 0, 1, 0, 1, 1, 1, 0]
count_0 = arr.count(0)
count_1 = arr.count(1)

minflips = min(count_0, count_1)
if count_0 == count_1:
    print("Minimum flips:", minflips )

elif count_0 < count_1:
    print("Minimum flips:", minflips )
else:
    print("Minimum flips:", minflips )
