
def longest_consecutive_ones(n):
    count = 0
    max_count = 0
    while n != 0:
        if n & 1:
            count += 1
            if count>max_count:
                max_count = count
        else: 
            count = 0
        n = n>>1
        return max_count
    
num = int(input("Enter a number:"))
print("Longest consecutive 1s:", longest_consecutive_ones(num))