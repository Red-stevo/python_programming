class NumberNotFoundException(Exception):
    pass


class Test:

    def __int__(self, num):
        self.num = num

    def check_number(self, num):
        try:
            if num == self.num:
                print("Number Is 6.")
            else:
                raise NumberNotFoundException
        except Exception as e:
            print(e)
