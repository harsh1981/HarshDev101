try:
    file=open("NewFile.txt", mode="r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("What are you looking for, File not found mate")
finally:
    file.close()
