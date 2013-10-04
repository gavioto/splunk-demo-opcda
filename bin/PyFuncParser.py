# $ANTLR 3.5 PyFunc.g 2013-09-03 15:56:40

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
AS=4
COMMA=5
DOT=6
ESC_SEQ=7
EXPONENT=8
FLOAT=9
HEX_DIGIT=10
INT=11
LONGINT=12
LPAREN=13
NAME=14
OCTAL_ESC=15
RPAREN=16
SEMICOLON=17
STRING=18
UNICODE_ESC=19
WS=20

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "AS", "COMMA", "DOT", "ESC_SEQ", "EXPONENT", "FLOAT", "HEX_DIGIT", "INT", 
    "LONGINT", "LPAREN", "NAME", "OCTAL_ESC", "RPAREN", "SEMICOLON", "STRING", 
    "UNICODE_ESC", "WS"
]


class Function(object):
    def __init__(self):
        self.packages = []
        self.name = None
        self.alias = None
        self.arguments = []


class PyFuncParser(Parser):
    grammarFileName = "PyFunc.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(PyFuncParser, self).__init__(input, state, *args, **kwargs)

        self.delegates = []

    # $ANTLR start "pyfunc"
    # PyFunc.g:6:1: pyfunc : ( pkgdef '.' )? NAME parameters ( asvar )? ;
    def pyfunc(self):
        func = Function()
        try:
            try:
                # PyFunc.g:6:8: ( ( pkgdef '.' )? NAME parameters ( asvar )? )
                # PyFunc.g:6:10: ( pkgdef '.' )? NAME parameters ( asvar )?
                pass 
                # PyFunc.g:6:10: ( pkgdef '.' )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == NAME) :
                    LA1_1 = self.input.LA(2)

                    if (LA1_1 == DOT) :
                        alt1 = 1
                if alt1 == 1:
                    # PyFunc.g:6:11: pkgdef '.'
                    pass 
                    self._state.following.append(self.FOLLOW_pkgdef_in_pyfunc24)
                    self.pkgdef(func.packages)

                    self._state.following.pop()

                    self.match(self.input, DOT, self.FOLLOW_DOT_in_pyfunc26)

                token = self.match(self.input, NAME, self.FOLLOW_NAME_in_pyfunc30)
                func.name = token.text
                
                self._state.following.append(self.FOLLOW_parameters_in_pyfunc32)
                self.parameters(func.arguments)

                self._state.following.pop()

                # PyFunc.g:6:40: ( asvar )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == AS) :
                    alt2 = 1
                if alt2 == 1:
                    # PyFunc.g:6:41: asvar
                    pass 
                    self._state.following.append(self.FOLLOW_asvar_in_pyfunc35)
                    self.asvar(func)

                    self._state.following.pop()

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return func

    # $ANTLR end "pyfunc"



    # $ANTLR start "pkgdef"
    # PyFunc.g:8:1: pkgdef : NAME ( '.' NAME )* ;
    def pkgdef(self, pkgs):
        try:
            try:
                # PyFunc.g:8:8: ( NAME ( '.' NAME )* )
                # PyFunc.g:8:10: NAME ( '.' NAME )*
                pass 
                token = self.match(self.input, NAME, self.FOLLOW_NAME_in_pkgdef46)
                pkgs.append(token.text)
                
                # PyFunc.g:8:15: ( '.' NAME )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == DOT) :
                        LA3_1 = self.input.LA(2)

                        if (LA3_1 == NAME) :
                            LA3_2 = self.input.LA(3)

                            if (LA3_2 == DOT) :
                                alt3 = 1

                    if alt3 == 1:
                        # PyFunc.g:8:16: '.' NAME
                        pass 
                        self.match(self.input, DOT, self.FOLLOW_DOT_in_pkgdef49)

                        token = self.match(self.input, NAME, self.FOLLOW_NAME_in_pkgdef51)
                        pkgs.append(token.text)

                    else:
                        break #loop3

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "pkgdef"



    # $ANTLR start "parameters"
    # PyFunc.g:10:1: parameters : '(' ( arguments )? ')' ;
    def parameters(self, args):
        try:
            try:
                # PyFunc.g:10:12: ( '(' ( arguments )? ')' )
                # PyFunc.g:10:14: '(' ( arguments )? ')'
                pass 
                self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_parameters62)

                # PyFunc.g:10:18: ( arguments )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == FLOAT or (INT <= LA4_0 <= LONGINT) or LA4_0 == NAME or LA4_0 == STRING) :
                    alt4 = 1
                if alt4 == 1:
                    # PyFunc.g:10:19: arguments
                    pass 
                    self._state.following.append(self.FOLLOW_arguments_in_parameters65)
                    self.arguments(args)

                    self._state.following.pop()

                self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_parameters69)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "parameters"



    # $ANTLR start "arguments"
    # PyFunc.g:12:1: arguments : argument ( ',' argument )* ;
    def arguments(self, args):
        try:
            try:
                # PyFunc.g:12:11: ( argument ( ',' argument )* )
                # PyFunc.g:12:13: argument ( ',' argument )*
                pass 
                self._state.following.append(self.FOLLOW_argument_in_arguments78)
                self.argument(args)

                self._state.following.pop()

                # PyFunc.g:12:22: ( ',' argument )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == COMMA) :
                        alt5 = 1


                    if alt5 == 1:
                        # PyFunc.g:12:23: ',' argument
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arguments81)

                        self._state.following.append(self.FOLLOW_argument_in_arguments83)
                        self.argument(args)

                        self._state.following.pop()

                    else:
                        break #loop5

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "arguments"



    # $ANTLR start "argument"
    # PyFunc.g:14:1: argument : ( var | numeric | string ) ;
    def argument(self, args):
        try:
            try:
                # PyFunc.g:14:10: ( ( var | numeric | string ) )
                # PyFunc.g:14:12: ( var | numeric | string )
                pass 
                # PyFunc.g:14:12: ( var | numeric | string )
                alt6 = 3
                LA6 = self.input.LA(1)
                if LA6 == NAME:
                    alt6 = 1
                elif LA6 == FLOAT or LA6 == INT or LA6 == LONGINT:
                    alt6 = 2
                elif LA6 == STRING:
                    alt6 = 3
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # PyFunc.g:14:13: var
                    pass 
                    self._state.following.append(self.FOLLOW_var_in_argument95)
                    self.var(args)

                    self._state.following.pop()


                elif alt6 == 2:
                    # PyFunc.g:14:19: numeric
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_in_argument99)
                    self.numeric(args)

                    self._state.following.pop()


                elif alt6 == 3:
                    # PyFunc.g:14:29: string
                    pass 
                    self._state.following.append(self.FOLLOW_string_in_argument103)
                    self.string(args)

                    self._state.following.pop()

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "argument"



    # $ANTLR start "asvar"
    # PyFunc.g:16:1: asvar : AS NAME ;
    def asvar(self, func):
        try:
            try:
                # PyFunc.g:16:7: ( AS NAME )
                # PyFunc.g:16:9: AS NAME
                pass 
                self.match(self.input, AS, self.FOLLOW_AS_in_asvar113)

                token = self.match(self.input, NAME, self.FOLLOW_NAME_in_asvar115)
                func.alias = token.text

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "asvar"



    # $ANTLR start "var"
    # PyFunc.g:18:1: var : NAME ;
    def var(self, args):
        try:
            try:
                # PyFunc.g:18:5: ( NAME )
                # PyFunc.g:18:7: NAME
                pass 
                token = self.match(self.input, NAME, self.FOLLOW_NAME_in_var124)
                args.append(('var', token.text))

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "var"



    # $ANTLR start "numeric"
    # PyFunc.g:20:1: numeric : ( INT | FLOAT | LONGINT );
    def numeric(self, args):
        try:
            try:
                # PyFunc.g:20:9: ( INT | FLOAT | LONGINT )
                # PyFunc.g:
                pass 
                if self.input.LA(1) == FLOAT or (INT <= self.input.LA(1) <= LONGINT):
                    token = self.input.consume()
                    args.append(('numeric', token.text))
                    
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "numeric"



    # $ANTLR start "string"
    # PyFunc.g:23:1: string : STRING ;
    def string(self, args):
        try:
            try:
                # PyFunc.g:23:8: ( STRING )
                # PyFunc.g:23:10: STRING
                pass 
                token = self.match(self.input, STRING, self.FOLLOW_STRING_in_string154)
                args.append(('string', token.text))

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "string"

    FOLLOW_pkgdef_in_pyfunc24 = frozenset([6])
    FOLLOW_DOT_in_pyfunc26 = frozenset([14])
    FOLLOW_NAME_in_pyfunc30 = frozenset([13])
    FOLLOW_parameters_in_pyfunc32 = frozenset([1, 4])
    FOLLOW_asvar_in_pyfunc35 = frozenset([1])
    FOLLOW_NAME_in_pkgdef46 = frozenset([1, 6])
    FOLLOW_DOT_in_pkgdef49 = frozenset([14])
    FOLLOW_NAME_in_pkgdef51 = frozenset([1, 6])
    FOLLOW_LPAREN_in_parameters62 = frozenset([9, 11, 12, 14, 16, 18])
    FOLLOW_arguments_in_parameters65 = frozenset([16])
    FOLLOW_RPAREN_in_parameters69 = frozenset([1])
    FOLLOW_argument_in_arguments78 = frozenset([1, 5])
    FOLLOW_COMMA_in_arguments81 = frozenset([9, 11, 12, 14, 18])
    FOLLOW_argument_in_arguments83 = frozenset([1, 5])
    FOLLOW_var_in_argument95 = frozenset([1])
    FOLLOW_numeric_in_argument99 = frozenset([1])
    FOLLOW_string_in_argument103 = frozenset([1])
    FOLLOW_AS_in_asvar113 = frozenset([14])
    FOLLOW_NAME_in_asvar115 = frozenset([1])
    FOLLOW_NAME_in_var124 = frozenset([1])
    FOLLOW_STRING_in_string154 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("PyFuncLexer", PyFuncParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
