# # import sys
# #
# # sys.path.append("/home/redsteve/.bashrc")
# #
# #
# # def personal_method():
# #     phone_number = {"stephen": "0110555949", "bob": "0110321096"}
# #     print(phone_number.values())
# #
# #
# # print(dir(sys))
# #  personal_method()
# # from file_exercise import create_file as c
# # from file_exercise import files_and_json as f
# # write into the file
# # c.write_file()
# # getting the occurrences
# # count = c.read_file()
# #
# # print(f"The number {count[0]} occurred {count[1]} times")
#
# # updating the file
# # c.update_file()
#
# # f.create_file()
#
# # f.read_json()
#
#
# """
# working with object-oriented programming.
# """
# from oop_concepts.python_inheritance import Child
#
# # from oop_concepts import python_inheritance as inheritance, Child
# #
# # v8 = Car("Toyota V8", "250km/hr", "good")
# #
# # v8.drive()
# # v8.break_down()
# #
# # vitz = Car("Toyota Vitz", "100km/hr", "bad")
# #
# # vitz.drive()
# # vitz.break_down()
#
#
# """
# Working with python inheritance.
# """
# #
# # if __name__ == "__main__":
# #     zion = Child()
# #     zion.skill()
#
#
# """
# Working with python exception handling
# """
#
# from oop_concepts.python_customer_exceptions import Test
#
# test = Test(6)
#
# test.check_number("b")
#
"""
Working with iterators.
"""

from oop_concepts.working_with_iterators import Remote_control

remote = Remote_control()

itr = iter(remote)

try:
    next(itr)
    next(itr)
    next(itr)
    next(itr)
    next(itr)
    next(itr)
    next(itr)
    next(itr)
    next(itr)
    next(itr)
except StopIteration as e:
    print("You Have Reached The End Of The Channel List")
