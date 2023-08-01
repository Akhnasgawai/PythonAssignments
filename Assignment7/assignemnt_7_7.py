# """7"""
class Reverse:
    def reverse(s):
        s2 = " "
        s = s.split(" ")
        s = s[::-1]
        return s2.join(s)


print(Reverse.reverse("hello .py"))
