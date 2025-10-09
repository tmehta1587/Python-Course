
def fac(n):
    if(n>0):
        if(n==1 or n==0):
            return 1
        return n*fac(n-1)
    else:
        print("Enter a valid input it should be a positive number")

n = int(input("Enter your number:"))
print("Factorial of", n, "is:", fac(n))