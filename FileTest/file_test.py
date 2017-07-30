#f_handle = open("test.txt","w")

#f_handle.write("Sheila Marie Robles\n")
#f_handle.write("My preferred language is: ")
#f_handle.write("Java")

#f_handle.close() # multiple pointers and opbjects that can hold multiple files

#f_handle = open("test.txt","a")

#f_handle.write("\n")
#f_handle.write("Python is so easy\n")
#f_handle.write("I'm learning so much!\n")

#f_handle.close()

#f_handle = open("test.txt", "r")

#print f_handle.readline().strip()
#print f_handle.readline().strip() # removes new line

#f_handle.close()

f_handle = open("test.txt","w+")

f_handle.write("Sheila Marie Robles\n")
f_handle.write("My preferred language is: ")
f_handle.write("Java")

f_handle.seek(0)
print f_handle.read()

f_handle.close()