
def longest_consecutive_ones(n):
    count = 0
    max_count = 0
    for bit in binary: 
        if bit == '1':
            count += 1
            if count>max_count:
                max_count = count
        else: 
            count = 0
    return max_count
    
num = int(input("Enter a number:"))
binary = bin(num)[2:]
print("Longest consecutive 1s:", longest_consecutive_ones(binary) )