def semantic_analysis(tokens):

    for i in range(len(tokens)):

        token_type, value = tokens[i]

        # Check division by zero
        if value == "/" and i + 1 < len(tokens):

            next_type, next_value = tokens[i + 1]

            if next_type == "NUMBER" and next_value == "0":

                return False, "Semantic Error: Division by zero"

    return True, "Semantic Analysis Successful"