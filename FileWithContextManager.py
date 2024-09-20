# This is with the help of context manager


with open("ExamplewithContextManager.txt", "w") as file:
    file.write("This a new file created with the help of context manager\n")
    file.write("This a new file with new line 2 created with the help of context manager\n")
    file.write("This a new file with new line 3 created with the help of context manager\n")
 