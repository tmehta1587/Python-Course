
file_read = open('Codingal.txt', 'r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')
file_write.write("File in write mode....")
file_write.write("Hi! I am Penguin. I am 1 year old.")
file_write.close()

file_append = open('Codingal.txt', 'a')
file_append.write("\n File in append mode....")
file_append.write("Hi! I am Penguin. I am 1 year old")
file_append.close()

file = open('Codingal.txt', 'r')
print("Reading first line")
print(file.readline())
file.close()

file= open('Codingal.txt', 'r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close

file=open('Codingal.txt', 'r')
print("Looping through lines...")
for line in file: 
    print(line)
file.close()
