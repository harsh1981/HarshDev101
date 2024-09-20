file=open("FileHandlingExample.txt", "r")
text=file.read()
print(text)



# reading file line by line by below code

file=open("FileHandlingExample.txt", "r")
line=file.readline()
while line !='':
    print(line,end='\n')
    line=file.readline()
    file.closed



# reading file line by line by below code with Mode="r" means read mode which is same as "r" or mode="w" means write

file=open("FileHandlingExample.txt", mode="r")
line=file.readline()
while line !='':
    print(line,end='\n')
    line=file.readline()
    file.closed



# Write (mode w or mode a)/creating or appending a new file 
file=open("NewFile.txt", "w")
file.write("This is a new file information example for writing a new file. \n")
file.close()


# Write (mode a) for appending a new file 
file=open("NewFile.txt", "a")
file.write("This is a new file information example for appending a new file. \n")
file.close()