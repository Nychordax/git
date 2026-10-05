append_text = '\nThis is appended file.'
my_file = open('my file.txt','a')
my_file.write(append_text)
print(my_file)
my_file.close()

