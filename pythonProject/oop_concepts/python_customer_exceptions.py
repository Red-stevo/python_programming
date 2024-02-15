class NumberNotFoundException(Exception):
    def __init__(self, message):
        self.message = message


class Test:
    def __init__(self, num):
        self.num = num

    def check_number(self, num):
        try:
            if int(num) == self.num:
                print("Number Is 6.")
            else:
                raise NumberNotFoundException("The Number You Entered Was Not found")
        except NumberNotFoundException as e:
            print(e.message)
        except ValueError as e:
            print("The Number You Entered Is Not A Numerical")
