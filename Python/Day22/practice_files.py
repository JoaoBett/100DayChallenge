file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

#w -> write
#a -> append
#r -> read

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_files.txt", mode="a") as file:
    file.write("\nNew text.")