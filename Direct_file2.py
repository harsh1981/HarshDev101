#print(locals())
import Direct_file1
print(f"File name is set to: {__name__}")

if __name__ == "__main__":
    print ("This file is excuted Directly")
else:
    print ("This file is excuted when imported")