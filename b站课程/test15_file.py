text = 'This is my first test.\nThis is my second test.\nThis is my third test.'
print(text)
my_file = open('my file.txt','w') # w write a file, r read a file, a append to a file
my_file.write(text)
my_file.close() # close the file after writing