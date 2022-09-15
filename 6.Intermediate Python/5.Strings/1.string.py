from timeit import default_timer as timer
# strings are immutable, ordered, text representation
string = "Mohammad jonayed"
print(string)

# using special characters:
s1 = "i'm a programmer"
print(s1)
s1 = 'i\'m a programmer'
print(s1)

# multi line string:
s2 = """
i
 am 
  jonayed
"""
print(s2)

s2 = """
i\
 am  
   jonayed
"""
print(s2)

# accessing string elements using index :
s3 = "I am jonayed"
print(s3[0])
print(s3[-1])

# strings are immutable :
# s3 = "i am jonayed"
# s3[0] = "i am"
# print(s3) this portion of code will give error as strings are immutable

# string slicing :
s4 = "Hello World"
print(s4[1:5])
print(s4[:5])
print(s4[1:])
print(s4[1:-1])
print(s4[-5:-1])

# printing strings every second character :
s4 = "Hello world"
print(s4[::2])
# reversing a string :
print(s4[::-1])

# string concatenation :
greet = "Hello"
name = "TOM"
sentence = greet + " " + name
print(sentence)

# printing each character of a string :
string = "Mohammad"
for i in string:
    print(i, end="\t")

# check if a sub string or a letter is in a string :
string = "Jonayed"
if "k" in string:
    print("\n Yes")
else:
    print("\n No")

if "Jon" in string:
    print("Yes")
else:
    print("No")

# remove white spaces from a string :
string = "    jonayed       sarkar    "
print(string.strip())  # note it removes white spaces not the spaces between two sub strings

# converting string in upper case and lower case letters :
string = "Hello"
print(string.upper())
print(string.lower())

# check if a string starts or ends with a certain character or sub-string :
string = "Hello"
print(string.startswith("h"))
print(string.startswith("H"))
print(string.startswith("Hell"))
print(string.endswith("o"))
print(string.endswith("hell"))

# find a character's position in a string :
string = "Jonayed"
print(string.find("o"))

# to count how many times a character occurs :

string = "Hello World"
print(string.count("l"))
print(string.count("0"))
print(string.count("k"))

# replacing a string with another string but remember one thing that this will not change the existing string:

string = "Hello world"
print(string.replace("Hello","hi"))
# if we give wrong string then it will print the original string as it is

# converting each string word into elements of a list:
string = "hello world and universe"
my_list = string.split(" ")
print(my_list)

string = "hello,world,and,universe"
my_list = string.split(",")
print(my_list)

# list to string conversion:
string = "hello,world,and,universe"
my_list = string.split(",")
print(my_list)
new_string = " ".join(my_list)
print(new_string)

new_list = ['a']*1000000
#print(new_list)

#bad practice :
start = timer()
string = ""
for i in new_list:
    string = string + i
stop = timer()
print("time taken : ",(stop-start))


#good practice:
start = timer()
string = "".join(new_list)
stop = timer()
print("time taken : ",(stop-start))