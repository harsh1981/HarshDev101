import os

os.mkdir("Testdirectory")

file=open("Testdirectory/example.txt", "w")
lines = ("This\n is\n a\n line\n")
file.write(lines)
file.close()
