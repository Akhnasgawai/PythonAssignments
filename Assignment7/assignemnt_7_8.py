"""8"""


class Play_string:
    def get_string(self):
        st = input("Enter the string: ")
        self.st = st

    def print_string(self):
        return self.st[::-1]


first_string = Play_string()
first_string.get_string()
print(first_string.print_string())
