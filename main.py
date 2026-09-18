
from lexer import lexical_analysis
from parser import Parser
from semantic import semantic_analysis
from intermediate import generate_code
from optimizer import optimize
from codegen import generate_target_code


expression = input("Enter expression: ")


# -----------------------------
# LEXICAL ANALYSIS
# -----------------------------

tokens = lexical_analysis(expression)

print("\n--- LEXICAL ANALYSIS ---")

if tokens:
    for token in tokens:
        print(token)
else:
    exit()


# -----------------------------
# SYNTAX ANALYSIS
# -----------------------------

print("\n--- SYNTAX ANALYSIS ---")

parser = Parser(tokens)

if parser.parse():
    print("Valid Expression")
else:
    print("Syntax Error: Invalid Expression")
    exit()


# -----------------------------
# SEMANTIC ANALYSIS
# -----------------------------

print("\n--- SEMANTIC ANALYSIS ---")

valid, message = semantic_analysis(tokens)

print(message)

if not valid:
    exit()


# -----------------------------
# INTERMEDIATE CODE GENERATION
# -----------------------------

print("\n--- INTERMEDIATE CODE ---")

code = generate_code(tokens)

for line in code:
    print(line)


# -----------------------------
# CODE OPTIMIZATION
# -----------------------------

print("\n--- OPTIMIZED CODE ---")

optimized_code = optimize(code)

for line in optimized_code:
    print(line)


# -----------------------------
# TARGET CODE GENERATION
# -----------------------------

print("\n--- TARGET CODE ---")

target_code = generate_target_code(optimized_code)

for line in target_code:
    print(line)


# -----------------------------
# COMPILATION COMPLETE
# -----------------------------

print("\n--- COMPILATION SUCCESSFUL ---")
