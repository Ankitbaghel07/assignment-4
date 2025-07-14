# Write and Append Data to a File
file=open("output.txt","w")
a=str(input("enter text to write in file: "))
write=file.write(a)
print("data succesfully writen to output.txt")
file.close()

file=open("output.txt","a")
b=str(input("enter additional text to append: "))
append=file.write(b)
print("Data succesfully appended.")
file.close()

file=open("output.txt","r")
read= file.readlines()
print("Final content of output.txt: ")
print(read)
file.close()