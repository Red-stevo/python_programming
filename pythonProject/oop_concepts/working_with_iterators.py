class Remote_control:
    def __init__(self):
        self.index = -1
        self.channels = ["inooro tv", "citizen tv", "meru tv", "kikuyu tv", "jata tv", "jambo tv", "Kameme tv"]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        print(self.channels[self.index])
