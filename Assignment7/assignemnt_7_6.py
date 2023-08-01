"""6"""


class Math:
    def power(x, n):
        if n == 0:
            return 1
        if x == 0:
            return 0
        return x * Math.power(x, n - 1)


print(Math.power(5, 3))
