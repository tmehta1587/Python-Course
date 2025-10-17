

count = 0  # Global counter for tracking recursive calls

def fac(n):
    global count
    count += 1  # Count each recursive call

    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)

print("Total calls before factorial:", count)
print("Factorial result:", fac(5))
print("Total recursive calls (time complexity count):", count)
