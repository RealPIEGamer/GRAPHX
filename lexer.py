class Lexer:
    def __init__(self, source):
        self.source = list(source)
        self.line = 0
        self.index = 0

    def current(self):
        return self.source[self.index]

    def next(self):
        return self.source[self.index + 1]

    def tokenize(self):
        for _ in self.source:
            print(self.current())
            self.index += 1