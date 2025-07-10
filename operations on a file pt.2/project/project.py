
with open('create.txt', 'w') as file:
    file.write("How to create a new file!")
file.close()

with open('create.txt', 'r') as file: 
    data= file.readlines()
    print("Words in this file are...")
    for line in data: 
        word = line.split()
        print(word)
file.close
