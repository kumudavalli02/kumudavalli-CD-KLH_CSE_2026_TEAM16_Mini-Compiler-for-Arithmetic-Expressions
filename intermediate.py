def generate_code(tokens):

    values = []
    operators = []
    code = []
    temp = 1

    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2
    }

    for token_type, value in tokens:

        if token_type == "NUMBER" or token_type == "ID":
            values.append(value)

        elif value == "(":
            operators.append(value)

        elif value == ")":

            while operators and operators[-1] != "(":
                op = operators.pop()

                b = values.pop()
                a = values.pop()

                result = "t" + str(temp)
                temp += 1

                code.append(result + " = " + a + " " + op + " " + b)

                values.append(result)

            operators.pop()

        else:

            while (operators and operators[-1] != "(" and
                   precedence[operators[-1]] >= precedence[value]):

                op = operators.pop()

                b = values.pop()
                a = values.pop()

                result = "t" + str(temp)
                temp += 1

                code.append(result + " = " + a + " " + op + " " + b)

                values.append(result)

            operators.append(value)

    while operators:

        op = operators.pop()

        b = values.pop()
        a = values.pop()

        result = "t" + str(temp)
        temp += 1

        code.append(result + " = " + a + " " + op + " " + b)

        values.append(result)

    return code