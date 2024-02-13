# In this file we will create a file, then enter some numbers in the file separated by commas.

# create a file called nums_data, and enter the values.

def write_file():
    with open("nums_data.txt", "w") as nums_file:
        for i in range(6):
            nums_file.write(input("Enter num 1 : ") + "," + input("Enter num 2 : ") + "\n")


def read_file():
    # Ask for the number to be search
    num = input("Enter The Number To Search : ")
    count = 0


    # open the file for reading.
    with open("nums_data.txt", "r") as nums_file:

        # ensure the number entered is correct.
        try:
            num = int(num)
        except:
            print("You Entered A Non Integer value.\nTry Again.")
            return[0,0]
        # search for the number in the file.
        for line in nums_file.read():
            tokens = line.split(",")
            for nums in tokens:
                if nums == num:
                    ++count
    return [num, count]
