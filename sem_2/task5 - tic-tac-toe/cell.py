class Cell:
    def __init__(self):
        self.value = 0 

    def __bool__(self):
        return self.value == 0  