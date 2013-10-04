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


class PyFuncLexer(Lexer):

    grammarFileName = "PyFunc.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(PyFuncLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )

        self.dfa15 = self.DFA15(
            self, 15,
            eot = self.DFA15_eot,
            eof = self.DFA15_eof,
            min = self.DFA15_min,
            max = self.DFA15_max,
            accept = self.DFA15_accept,
            special = self.DFA15_special,
            transition = self.DFA15_transition
            )






    # $ANTLR start "AS"
    def mAS(self, ):
        try:
            _type = AS
            _channel = DEFAULT_CHANNEL

            # PyFunc.g:25:4: ( ( 'A' | 'a' ) ( 'S' | 's' ) )
            # PyFunc.g:25:6: ( 'A' | 'a' ) ( 'S' | 's' )
            pass 
            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AS"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):
        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # PyFunc.g:26:8: ( '(' )
            # PyFunc.g:26:10: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):
        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # PyFunc.g:27:8: ( ')' )
            # PyFunc.g:27:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # PyFunc.g:28:7: ( ',' )
            # PyFunc.g:28:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "SEMICOLON"
    def mSEMICOLON(self, ):
        try:
            _type = SEMICOLON
            _channel = DEFAULT_CHANNEL

            # PyFunc.g:29:11: ( ';' )
            # PyFunc.g:29:13: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SEMICOLON"



    # $ANTLR start "DOT"
    def mDOT(self, ):
        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # PyFunc.g:30:5: ( '.' )
            # PyFunc.g:30:7: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOT"



    # $ANTLR start "NAME"
    def mNAME(self, ):
        try:
            _type = NAME
            _channel = DEFAULT_CHANNEL

            # PyFunc.g:31:6: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )* )
            # PyFunc.g:31:8: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # PyFunc.g:31:32: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # PyFunc.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NAME"



    # $ANTLR start "INT"
    def mINT(self, ):
        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # PyFunc.g:33:5: ( ( '0' .. '9' )+ )
            # PyFunc.g:33:9: ( '0' .. '9' )+
            pass 
            # PyFunc.g:33:9: ( '0' .. '9' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # PyFunc.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INT"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):
        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # PyFunc.g:37:5: ( ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )? | '.' ( '0' .. '9' )+ ( EXPONENT )? | ( '0' .. '9' )+ EXPONENT )
            alt9 = 3
            alt9 = self.dfa9.predict(self.input)
            if alt9 == 1:
                # PyFunc.g:37:9: ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )?
                pass 
                # PyFunc.g:37:9: ( '0' .. '9' )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((48 <= LA3_0 <= 57)) :
                        alt3 = 1


                    if alt3 == 1:
                        # PyFunc.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                self.match(46)

                # PyFunc.g:37:25: ( '0' .. '9' )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((48 <= LA4_0 <= 57)) :
                        alt4 = 1


                    if alt4 == 1:
                        # PyFunc.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop4


                # PyFunc.g:37:37: ( EXPONENT )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 69 or LA5_0 == 101) :
                    alt5 = 1
                if alt5 == 1:
                    # PyFunc.g:37:37: EXPONENT
                    pass 
                    self.mEXPONENT()






            elif alt9 == 2:
                # PyFunc.g:38:9: '.' ( '0' .. '9' )+ ( EXPONENT )?
                pass 
                self.match(46)

                # PyFunc.g:38:13: ( '0' .. '9' )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if ((48 <= LA6_0 <= 57)) :
                        alt6 = 1


                    if alt6 == 1:
                        # PyFunc.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1


                # PyFunc.g:38:25: ( EXPONENT )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 69 or LA7_0 == 101) :
                    alt7 = 1
                if alt7 == 1:
                    # PyFunc.g:38:25: EXPONENT
                    pass 
                    self.mEXPONENT()






            elif alt9 == 3:
                # PyFunc.g:39:9: ( '0' .. '9' )+ EXPONENT
                pass 
                # PyFunc.g:39:9: ( '0' .. '9' )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if ((48 <= LA8_0 <= 57)) :
                        alt8 = 1


                    if alt8 == 1:
                        # PyFunc.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1


                self.mEXPONENT()



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # PyFunc.g:42:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # PyFunc.g:42:9: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            #action start
            Lexer.skip(self);
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    # $ANTLR start "STRING"
    def mSTRING(self, ):
        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # PyFunc.g:50:5: ( '\"' ( ESC_SEQ |~ ( '\\\\' | '\"' ) )* '\"' )
            # PyFunc.g:50:8: '\"' ( ESC_SEQ |~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)

            # PyFunc.g:50:12: ( ESC_SEQ |~ ( '\\\\' | '\"' ) )*
            while True: #loop10
                alt10 = 3
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 92) :
                    alt10 = 1
                elif ((0 <= LA10_0 <= 33) or (35 <= LA10_0 <= 91) or (93 <= LA10_0 <= 65535)) :
                    alt10 = 2


                if alt10 == 1:
                    # PyFunc.g:50:14: ESC_SEQ
                    pass 
                    self.mESC_SEQ()



                elif alt10 == 2:
                    # PyFunc.g:50:24: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop10


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRING"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):
        try:
            # PyFunc.g:55:10: ( ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+ )
            # PyFunc.g:55:12: ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # PyFunc.g:55:22: ( '+' | '-' )?
            alt11 = 2
            LA11_0 = self.input.LA(1)

            if (LA11_0 == 43 or LA11_0 == 45) :
                alt11 = 1
            if alt11 == 1:
                # PyFunc.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # PyFunc.g:55:33: ( '0' .. '9' )+
            cnt12 = 0
            while True: #loop12
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if ((48 <= LA12_0 <= 57)) :
                    alt12 = 1


                if alt12 == 1:
                    # PyFunc.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt12 >= 1:
                        break #loop12

                    eee = EarlyExitException(12, self.input)
                    raise eee

                cnt12 += 1





        finally:
            pass

    # $ANTLR end "EXPONENT"



    # $ANTLR start "ESC_SEQ"
    def mESC_SEQ(self, ):
        try:
            # PyFunc.g:59:5: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESC | OCTAL_ESC )
            alt13 = 3
            LA13_0 = self.input.LA(1)

            if (LA13_0 == 92) :
                LA13 = self.input.LA(2)
                if LA13 == 34 or LA13 == 39 or LA13 == 92 or LA13 == 98 or LA13 == 102 or LA13 == 110 or LA13 == 114 or LA13 == 116:
                    alt13 = 1
                elif LA13 == 117:
                    alt13 = 2
                elif LA13 == 48 or LA13 == 49 or LA13 == 50 or LA13 == 51 or LA13 == 52 or LA13 == 53 or LA13 == 54 or LA13 == 55:
                    alt13 = 3
                else:
                    nvae = NoViableAltException("", 13, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 13, 0, self.input)

                raise nvae


            if alt13 == 1:
                # PyFunc.g:59:9: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)

                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt13 == 2:
                # PyFunc.g:60:9: UNICODE_ESC
                pass 
                self.mUNICODE_ESC()



            elif alt13 == 3:
                # PyFunc.g:61:9: OCTAL_ESC
                pass 
                self.mOCTAL_ESC()




        finally:
            pass

    # $ANTLR end "ESC_SEQ"



    # $ANTLR start "OCTAL_ESC"
    def mOCTAL_ESC(self, ):
        try:
            # PyFunc.g:66:5: ( '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) )
            alt14 = 3
            LA14_0 = self.input.LA(1)

            if (LA14_0 == 92) :
                LA14_1 = self.input.LA(2)

                if ((48 <= LA14_1 <= 51)) :
                    LA14_2 = self.input.LA(3)

                    if ((48 <= LA14_2 <= 55)) :
                        LA14_4 = self.input.LA(4)

                        if ((48 <= LA14_4 <= 55)) :
                            alt14 = 1
                        else:
                            alt14 = 2

                    else:
                        alt14 = 3

                elif ((52 <= LA14_1 <= 55)) :
                    LA14_3 = self.input.LA(3)

                    if ((48 <= LA14_3 <= 55)) :
                        alt14 = 2
                    else:
                        alt14 = 3

                else:
                    nvae = NoViableAltException("", 14, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 14, 0, self.input)

                raise nvae


            if alt14 == 1:
                # PyFunc.g:66:9: '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 51):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt14 == 2:
                # PyFunc.g:67:9: '\\\\' ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt14 == 3:
                # PyFunc.g:68:9: '\\\\' ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse





        finally:
            pass

    # $ANTLR end "OCTAL_ESC"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):
        try:
            # PyFunc.g:72:11: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # PyFunc.g:
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "HEX_DIGIT"



    # $ANTLR start "UNICODE_ESC"
    def mUNICODE_ESC(self, ):
        try:
            # PyFunc.g:76:5: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
            # PyFunc.g:76:9: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
            pass 
            self.match(92)

            self.match(117)

            self.mHEX_DIGIT()


            self.mHEX_DIGIT()


            self.mHEX_DIGIT()


            self.mHEX_DIGIT()





        finally:
            pass

    # $ANTLR end "UNICODE_ESC"



    # $ANTLR start "LONGINT"
    def mLONGINT(self, ):
        try:
            _type = LONGINT
            _channel = DEFAULT_CHANNEL

            # PyFunc.g:79:5: ( INT ( 'l' | 'L' ) )
            # PyFunc.g:79:9: INT ( 'l' | 'L' )
            pass 
            self.mINT()


            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LONGINT"



    def mTokens(self):
        # PyFunc.g:1:8: ( AS | LPAREN | RPAREN | COMMA | SEMICOLON | DOT | NAME | INT | FLOAT | WS | STRING | LONGINT )
        alt15 = 12
        alt15 = self.dfa15.predict(self.input)
        if alt15 == 1:
            # PyFunc.g:1:10: AS
            pass 
            self.mAS()



        elif alt15 == 2:
            # PyFunc.g:1:13: LPAREN
            pass 
            self.mLPAREN()



        elif alt15 == 3:
            # PyFunc.g:1:20: RPAREN
            pass 
            self.mRPAREN()



        elif alt15 == 4:
            # PyFunc.g:1:27: COMMA
            pass 
            self.mCOMMA()



        elif alt15 == 5:
            # PyFunc.g:1:33: SEMICOLON
            pass 
            self.mSEMICOLON()



        elif alt15 == 6:
            # PyFunc.g:1:43: DOT
            pass 
            self.mDOT()



        elif alt15 == 7:
            # PyFunc.g:1:47: NAME
            pass 
            self.mNAME()



        elif alt15 == 8:
            # PyFunc.g:1:52: INT
            pass 
            self.mINT()



        elif alt15 == 9:
            # PyFunc.g:1:56: FLOAT
            pass 
            self.mFLOAT()



        elif alt15 == 10:
            # PyFunc.g:1:62: WS
            pass 
            self.mWS()



        elif alt15 == 11:
            # PyFunc.g:1:65: STRING
            pass 
            self.mSTRING()



        elif alt15 == 12:
            # PyFunc.g:1:72: LONGINT
            pass 
            self.mLONGINT()








    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\2\56\3\uffff"
        )

    DFA9_max = DFA.unpack(
        u"\1\71\1\145\3\uffff"
        )

    DFA9_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\3"
        )

    DFA9_special = DFA.unpack(
        u"\5\uffff"
        )


    DFA9_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


    # lookup tables for DFA #15

    DFA15_eot = DFA.unpack(
        u"\1\uffff\1\7\4\uffff\1\14\1\uffff\1\16\2\uffff\1\20\5\uffff"
        )

    DFA15_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA15_min = DFA.unpack(
        u"\1\11\1\123\4\uffff\1\60\1\uffff\1\56\2\uffff\1\60\5\uffff"
        )

    DFA15_max = DFA.unpack(
        u"\1\172\1\163\4\uffff\1\71\1\uffff\1\154\2\uffff\1\172\5\uffff"
        )

    DFA15_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\4\1\5\1\uffff\1\7\1\uffff\1\12\1\13\1\uffff"
        u"\1\6\1\11\1\10\1\14\1\1"
        )

    DFA15_special = DFA.unpack(
        u"\21\uffff"
        )


    DFA15_transition = [
        DFA.unpack(u"\2\11\2\uffff\1\11\22\uffff\1\11\1\uffff\1\12\5\uffff"
        u"\1\2\1\3\2\uffff\1\4\1\uffff\1\6\1\uffff\12\10\1\uffff\1\5\5\uffff"
        u"\1\1\31\7\4\uffff\1\7\1\uffff\1\1\31\7"),
        DFA.unpack(u"\1\13\37\uffff\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\15"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\15\1\uffff\12\10\13\uffff\1\15\6\uffff\1\17\30\uffff"
        u"\1\15\6\uffff\1\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\7\7\uffff\32\7\4\uffff\1\7\1\uffff\32\7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #15

    class DFA15(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(PyFuncLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
