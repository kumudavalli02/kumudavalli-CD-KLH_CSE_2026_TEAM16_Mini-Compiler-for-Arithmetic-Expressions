def lexical_analysis(expression):

    tokens = []
    i = 0

    while i < len(expression):

        ch = expression[i]

        # Ignore spaces
        if ch == " ":
            i += 1
            continue

        # Identifier
        if ch.isalpha():
            tokens.append(("ID", ch))
            i += 1

        # Number
        elif ch.isdigit():

            number = ""

            while i < len(expression) and expression[i].isdigit():
                number += expression[i]
                i += 1

            tokens.append(("NUMBER", number))

        # Operators
        elif ch in "+-*/":
            tokens.append(("OPERATOR", ch))
            i += 1

        # Left parenthesis
        elif ch == "(":
            tokens.append(("LPAREN", ch))
            i += 1

        # Right parenthesis
        elif ch == ")":
            tokens.append(("RPAREN", ch))
            i += 1

        # Invalid character
        else:
            print("Lexical Error: Invalid character", ch)
            return None

    return tokens