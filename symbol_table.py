symbol_table = {}


def add_symbol(name, value):
    symbol_table[name] = value


def get_symbol(name):
    return symbol_table.get(name)


def display_table():
    print("Symbol Table:")
    for name, value in symbol_table.items():
        print(name, "=", value)


# Test
add_symbol("a", 10)
add_symbol("b", 20)

display_table()