# In this file we will create a file, then enter some numbers in the file separated by commas.

# create a file called nums_data, and enter the values.

def write_file():
    with open("nums_data.txt", "a+") as nums_file:
        for i in range(6):
            nums_file.write(input("Enter num 1 : ") + "," + input("Enter num 2 : ")+"\n")

