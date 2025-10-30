
def equilibriumPoint(arr):
    leftSideSum = 0
    rightSideSum = 0
    n = len(arr)

    for i in range(n):
        leftSideSum = 0
        rightSidesum = 0

        for j in range(i + 1, n):
            rightSidesum += arr[j]
        
        if leftSideSum == rightSideSum:
            return 1 
        else: 
            return 0         

arr = [-4, 6, 2, 0, 0, 1, 1] 
if equilibriumPoint(arr):
    print("array is the equilibrium")
else: 
    print("array is not the equilibrium")
