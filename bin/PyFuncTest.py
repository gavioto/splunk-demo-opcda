import antlr3
from PyFuncLexer import PyFuncLexer
from PyFuncParser import PyFuncParser
 
pfun = 'a.b.c.MyFun (123, dyz, "abc") AS MyFunx '
char_stream = antlr3.ANTLRStringStream(pfun)
# or to parse a file:
# char_stream = antlr3.ANTLRFileStream(path_to_input)
# or to parse an opened file or any other file-like object:
# char_stream = antlr3.ANTLRInputStream(file)
 
lexer = PyFuncLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)

tokens.fillBuffer()

parser = PyFuncParser(tokens)
func = parser.pyfunc()
print "------- %s --------" % func.name
print func.packages
print func.name
print func.alias
print func.arguments

'''
print parser.toStrings(tokens.tokens)
for token in tokens.tokens:
    print "text=%s, type=%s\n" % (token.text, token.type)
    
'''

