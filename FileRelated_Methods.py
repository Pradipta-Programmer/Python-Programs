text= open("sampletext.txt") # reads given file by default, return error if not found
# if you want to do something else other than read
# use "w", "a", "x" for write, append, create file respectively
# use "t", "b", "+" for text-mode, binary-mode respectively
# any combination of the above abbreviations can be used
d= text.read() # copies the contents of file
print(d)
text.seek(0) # after .read(), pointer is at end of file so to go back at beginning
g= text.read(5) # copies the first 5 characters of file
print(g)
d= text.readline() # copies only the first line of the file
print(d)
d= text.readlines() # copies all lines of the file in list
print(d)
text.close() # always close the file
l= ["\nThis is in a list", "\nItems of list is in file now"] 
text= open("tempo.txt", "a") # opens with 'a' as in append
text.write("\nThank You") # this line is added in the given file
text.writelines(l) # adds the contents of the 'l' list in file
# if file not exist, creates file and add the line/s
# .writeline() not exists
text.close()
text= open("sampletext.txt", "r+")
# "+" with "r" or "w" will read and write altogether, with "a" will read and append
# "+" with "x" will read, write and create
b= text.read()
text.write("Hehe")
print(b)
text.close()
text= open("sample.txt", "x")
# line 4 has to be used with line 3 as they can't function on their own
# any combination with "x" will create file unless the file already exist so error
text.write("Feeling Great?")
print(b)
text.close()
f = open("sampletext.txt")
f.seek(0) # Go to beginning
print(f.read(5)) # Read first 5 characters
f.seek(10) # Move to 11th character
print(f.read(5)) # Read next 5 characters from 11th character
f.close()
f = open("sampletext.txt")
f.read(7)
print(f.tell()) # prints (index of the pointer - 1)
# Here, it will print 7
f.close()
with open("sampletext.txt", "w") as f:
    # this function only closes the file automatically, that's all
    f.write("Now I am writing in a file")
    f.writelines(l) # writes the contents of the 'l' list in file
    # if file not exist, creates file and write the line"""