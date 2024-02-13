# In this file we will create a file, then enter some numbers in the file separated by commas.

# create a file called nums_data, and enter the values.

def write_file():
    with open("nums_data.txt", "w") as nums_file:
        for i in range(6):
            nums_file.write(input("Enter num 1 : ") + "," + input("Enter num 2 : ")+"\n")


def read_file():
    # Ask for the number to be search
    num = int(input("Enter The Number To Search : "))
    count = 0
    # open the file for reading.
    with open("nums_data.txt", "r") as nums_file:
        file = nums_file.read()
        # search for the number in the file.
        number = file.split(",")

        for i in number:
            if len(i) > 1:
                nums = i.split("\n")
                for x in nums:
                    x = int(x)
                    if x == num:
                        count = count + 1
            else:
                i = int(i)
                if i == num:
                    count = count + 1

    return [num, count]


# changing the file to now contain
def update_file():
    r_file = open("nums_data.txt", "r")
    file_content = r_file.read()
    r_file.close()
    with open("update_file.txt", "w") as file:
        nums = file_content.split("\n")
        for i in nums:
            num = i.split(",")
            sum = 0
            for e in num:
                if e == " " or e == "":
                    continue
                e = int(e)
                sum = sum + e
            if e == "" or e == " ":
                continue
            file.write(f"Sum : {sum} | {i}\n")
