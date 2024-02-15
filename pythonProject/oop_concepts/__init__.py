class Car:
    def __init__(self, model, max_speed, condition):
        self.model = model
        self.max_speed = max_speed
        self.condition = condition

    def drive(self):
        print("The", self.model, "Is Moving At A Speed Of : ", self.max_speed)

    def break_down(self):
        if self.condition == "good":
            print("The", self.model, "is in ", self.condition, "Condition. It Will Not Breakdown Soon")
        elif self.condition == "bad":
            print("The", self.model, "is in ", self.condition, "Condition. It Will Breakdown Soon")
