valid_opening_delimiter = ["(", "[", "{"]


def check_delimiter(st):
    temp = []
    for i in st:
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


# li = ["([)]", "([]", "[])", "([})"]

li = ["()[]{}", "([{}])", "([]{})"]

for i in li:
    print(check_delimiter(i))
