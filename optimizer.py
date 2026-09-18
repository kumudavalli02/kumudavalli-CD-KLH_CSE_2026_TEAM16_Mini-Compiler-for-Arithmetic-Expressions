def optimize(intermediate_code):
    optimized_code = []

    for line in intermediate_code:
        parts = line.split()

        if len(parts) == 5:
            result = parts[0]
            left = parts[2]
            operator = parts[3]
            right = parts[4]

            if left.isdigit() and right.isdigit():

                a = int(left)
                b = int(right)

                if operator == "+":
                    value = a + b
                elif operator == "-":
                    value = a - b
                elif operator == "*":
                    value = a * b
                elif operator == "/" and b != 0:
                    value = a // b
                else:
                    optimized_code.append(line)
                    continue

                optimized_code.append(result + " = " + str(value))
            else:
                optimized_code.append(line)

        else:
            optimized_code.append(line)

    return optimized_code


# Test
intermediate_code = [
    "t1 = 5 + 3",
    "t2 = t1 * 2"
]

optimized = optimize(intermediate_code)

print("Optimized Code:")
for line in optimized:
    print(line)