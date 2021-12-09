# Imports lexer and lex for lexing, not to be confused with flexing
import lexer
from lexer import Lexer

# Tokenize file lol
with open('./examples/draw_window.gfx', 'r') as f:
    tokenized_source = Lexer(f.read()).tokenize()