


n = int(input("Enter your number:"))

def checkIfPower(n):
    if(n<=0):
        return False
    if(n==1):
        return True
    if(n%4 == 0):
        return checkIfPower(n/4)
    return False

if(checkIfPower(n)):
    print("Power of 4")
else:
    print("Not power of 4")
    