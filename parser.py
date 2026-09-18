class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):

        if self.pos < len(self.tokens):
            return self.tokens[self.pos]

        return None

    # Expression → Term ((+ | -) Term)*
    def expression(self):

        if not self.term():
            return False

        while True:

            token = self.current_token()

            if token and token[1] in "+-":

                self.pos += 1

                if not self.term():
                    return False

            else:
                break

        return True

    # Term → Factor ((* | /) Factor)*
    def term(self):

        if not self.factor():
            return False

        while True:

            token = self.current_token()

            if token and token[1] in "*/":

                self.pos += 1

                if not self.factor():
                    return False

            else:
                break

        return True

    # Factor → NUMBER | ID | (Expression)
    def factor(self):

        token = self.current_token()

        if token is None:
            return False

        if token[0] == "NUMBER":

            self.pos += 1
            return True

        if token[0] == "ID":

            self.pos += 1
            return True

        if token[0] == "LPAREN":

            self.pos += 1

            if not self.expression():
                return False

            token = self.current_token()

            if token is None or token[0] != "RPAREN":
                return False

            self.pos += 1

            return True

        return False

    def parse(self):

        if self.expression() and self.pos == len(self.tokens):
            return True

        return False