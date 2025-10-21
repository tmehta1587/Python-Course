


def power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2 * power_of_2(n-1)
    
def main():
    n = int(input("Enter a non-negative integer(n):"))

    if n<0:
        print("Please enter a non-negative integer.")
        return
    result = power_of_2(n)
    print("2^",n,"=",result)
main()
