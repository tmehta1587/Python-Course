


def paren(s,l,r,p,n):
    if(p==2*n):
        for ss in s:
            print(ss,end='')
        print("\n")
        return
    if(1>r):
        s[p]="}"
        paren(s,1,r+1,p+1,n)
    if(1<n):
        s[p]="{"
        paren(s,l+1,r,p+1,n)

n = int(input("Enter number of parenthesis: "))
s = [""]*2*n
print("\n")
paren(s,0,0,0,n)


