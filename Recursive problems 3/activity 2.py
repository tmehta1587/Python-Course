


keypad = ["","", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def printCombination(combination, curr, output, n):
    if curr == n:
        print("".join(output))
        return
    
    if combination[curr] == 0 or combination[curr] == 1:
        return
    
    for i in range(len(keypad[combination[curr]])):
        output.append(keypad[combination[curr]][i])
        printCombination(combination, curr + 1, output, n)
        output.pop()

combination = [2,3]
n = len(combination)
output = []
printCombination(combination,0,output,n)