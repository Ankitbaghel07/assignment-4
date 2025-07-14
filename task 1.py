#Read a File and Handle Errors 
try:
    file =open("sample.txt","r")
    read =file.readlines()
    print(read)
    file.close()
except FileNotFoundError:
    print("Error: the file sample.txt not found")