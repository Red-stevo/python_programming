write_file = open("text.txt", 'a')
read_text = open("text.txt", 'r')


write_file.write("Hey there steve.\n")

value = read_text.read()

tokens = value.split(".")

for i in tokens:
    print(i)


