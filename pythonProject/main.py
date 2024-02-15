# import sys
#
# sys.path.append("/home/redsteve/.bashrc")
#
#
# def personal_method():
#     phone_number = {"stephen": "0110555949", "bob": "0110321096"}
#     print(phone_number.values())
#
#
# print(dir(sys))
#  personal_method()
# from file_exercise import create_file as c
# from file_exercise import files_and_json as f
# write into the file
# c.write_file()
# getting the occurrences
# count = c.read_file()
#
# print(f"The number {count[0]} occurred {count[1]} times")

# updating the file
# c.update_file()

# f.create_file()

# f.read_json()


"""
working with object-oriented programming.
"""
from oop_concepts.python_inheritance import Child

# from oop_concepts import python_inheritance as inheritance, Child
#
# v8 = Car("Toyota V8", "250km/hr", "good")
#
# v8.drive()
# v8.break_down()
#
# vitz = Car("Toyota Vitz", "100km/hr", "bad")
#
# vitz.drive()
# vitz.break_down()


"""
Working with python inheritance.
"""

if __name__ == "__main__":
    zion = Child()
    zion.skill()
