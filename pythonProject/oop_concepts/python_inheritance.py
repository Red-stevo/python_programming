class Father:
    def skill(self):
        print("I Love Programming")


class Mother:
    def skills(self):
        print("I Love Machine Learning")


class Child(Father, Mother):
    def skill(self):
        super().skill()
        super().skill()
        print("I Love Mathematics")

