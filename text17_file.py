file = open('my file.txt','r') # r read a file\
content = file.readline() # read the first line of the file
second_read_line = file.readline() # read the second line of the file
read_lines = file.readlines() # read all the lines of the file
print(content)
print(second_read_line)
print(read_lines)
file.close() # close the file after reading