from antlr4 import ParseTreeWalker
from stOTTRLexer import stOTTRLexer
from stOTTRParser import stOTTRParser
from antlr4 import InputStream

stottr_input = "your stOTTR string here"
input_stream = InputStream(stottr_input)
lexer = stOTTRLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = stOTTRParser(token_stream)
parse_tree = parser.stOTTRDoc()

listener = MyListener()
walker = ParseTreeWalker()
walker.walk(listener, parse_tree)