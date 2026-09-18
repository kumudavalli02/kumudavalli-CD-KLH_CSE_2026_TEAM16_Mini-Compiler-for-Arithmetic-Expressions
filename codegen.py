def generate_target_code(intermediate_code):

    target_code = []

    for line in intermediate_code:

        parts = line.split()

        if len(parts) != 5:
            continue

        result = parts[0]
        left = parts[2]
        operator = parts[3]
        right = parts[4]

        target_code.append("LOAD " + left)

        if operator == "+":
            target_code.append("ADD " + right)

        elif operator == "-":
            target_code.append("SUB " + right)

        elif operator == "*":
            target_code.append("MUL " + right)

        elif operator == "/":
            target_code.append("DIV " + right)

        target_code.append("STORE " + result)

    return target_code