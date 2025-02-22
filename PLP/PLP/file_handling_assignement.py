# file=open("./PLP/my_file.txt", "w")
# file.write("Hello there\n")
# file.write("My name is Shaleen Atieno\n")
# file.write("I am a student\n")
# file.write("\'Singing\' is my hobby\n")
# file.write("My registration Number is S13/0897/22\n")


# file1=open("./PLP/my_file.txt", "r")
# print(file1.read())
# print(file1.readline())
# print(file1.readlines())
# file1.close()



# file2=open("./PLP/my_file.txt", "a")


# file2.write("PLp academy is the best\n")
# file2.write("Can't wait to build my own project")
# file2.close()




try:
    with open("example.txt", "r") as file3:
     print(file3.read())

except FileNotFoundError as e:
    print(e)
    print("Error:File not found")
except PermissionError as e:

    print(e)
    print("Error:File cannot be opened")
finally:
    print("File closing")



