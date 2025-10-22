


def Hanoi(n ,a,b,c):
    if n==1:
        print("Move disk 1 from rod",a,"to rod",b)
        return
    Hanoi(n-1, a,c,b)
    print("Move disk",n,"from rod",a,"to rod",b)
    Hanoi(n-1, c, b, a)

n=int(input("Enter a number: "))  
Hanoi(n, 'A', 'C', 'B')