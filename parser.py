class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.AST = []

    def build_AST(self):
        saved = {}
        parent = {}
        collect = False

        for token in self.tokens:
            if token['type'] == 'label': # checks if the token is a label, label??
                t = {token['value']: []}

                if parent != t:
                    parent = token['value']
                    self.AST.append(t)
            elif token['type'] == 'keyword': # checks for keywords
                if token['value'] == 'test':
                    t = {token['value']}