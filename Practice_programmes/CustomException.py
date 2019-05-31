class CustomError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
p = CustomError("This is custom exception")
print(p)
