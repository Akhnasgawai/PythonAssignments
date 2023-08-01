"""2"""

valid_opening_delimiter = ["(", "[", "{"]


class Brackets:
    def checkMatch(s):
        temp = []
        for i in s:
            if i in valid_opening_delimiter:
                temp.append(i)
            else:
                if temp:
                    if (
                        i == "}"
                        and temp[-1] == "{"
                        or i == "]"
                        and temp[-1] == "["
                        or i == ")"
                        and temp[-1] == "("
                    ):
                        del temp[-1]
                    else:
                        break
                else:
                    return False
        if temp:
            return False
        else:
            return True


print(Brackets.checkMatch("()[]"))
