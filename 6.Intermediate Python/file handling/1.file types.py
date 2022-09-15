"""
there are different types of files.
there are two types of files in python:
1.Binary files
2.Text files
operations performed on a file:
1. creating
2. reading
3. updating
4. deletion
create a file -> open file -> work -> close file.
open() file name and mode
syntax :
file = open(filename,mode)
modes :
r = read mode it is a default mode opens file for reading. gives error if file does not exists.
a = append mode. opens a file for appending creates a file if it is not exists.
w = write mode. Opens a file for writing and creates a file if it not exists
x = create mode. Creates the specified file returns an error if the file exists.

"""
f = open("1.test.txt","r")
# print(f.read()) # this command reads whole file
# print(f.readline(4)) # this command reads a line 

# print(f.readline()) # this command reads the next line
# print(f.readline(4),end="**") # it reads first 4 character from a line)

file1 = open("2.demo.txt","w") # it creates a file named demo
file1.write("something") # here we can use it to enter data to file
file1.write(" written ")

file2 = open("3.abcd.txt","a")
# file2.write("Computer") 
"""
here it will not delete the prevoius computer data. whenever we write into abc file it will append the new data with the previous data. 
"""
file2.write(" Science & engineering")

# copying all data from a file to another file :
# test.txt -> abc.txt
for data in f:
    file1.write(data)
# printing all data of file (f) :
for data in f:
    print(data)

# to read a file in binary mode
"""
in binary mode here is no character there is only numbers 1 or 0
"""
# lets try to read an image :
imgFile = open("nature.jpg","rb")  # rb stands for read binary mode
# for i in imgFile:
#     print(i)

# lets create an image from binary data from another image its like copying an image:

imgfile1 = open("field.jpg","wb")
for data in imgFile:
    imgfile1.write(data)