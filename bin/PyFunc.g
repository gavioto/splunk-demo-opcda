grammar PyFunc;
options {
    language=Python;
}

pyfunc : (pkgdef '.')? NAME parameters (asvar)? ;

pkgdef : NAME ('.' NAME)* ;

parameters : '(' (arguments)? ')' ;

arguments : argument (',' argument)* ;

argument : (var | numeric | string) ;

asvar : AS NAME ;

var : NAME ;

numeric : INT | FLOAT | LONGINT
    ;

string : STRING ;

AS : ('A'|'a') ('S'|'s') ;
LPAREN : '(' ;
RPAREN : ')' ;
COMMA : ',' ;
SEMICOLON : ';' ;
DOT : '.' ;
NAME : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')* ;

INT :   ('0'..'9')+  
    ;

FLOAT
    :   ('0'..'9')+ '.' ('0'..'9')* EXPONENT?  
    |   '.' ('0'..'9')+ EXPONENT? 
    |   ('0'..'9')+ EXPONENT 
    ;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) {skip();}
    ;

STRING
    :  '"' ( ESC_SEQ | ~('\\'|'"') )* '"' 
    ;

fragment
EXPONENT : ('e'|'E') ('+'|'-')? ('0'..'9')+ ;

fragment
ESC_SEQ
    :   '\\' ('b'|'t'|'n'|'f'|'r'|'\"'|'\''|'\\')
    |   UNICODE_ESC
    |   OCTAL_ESC
    ;

fragment
OCTAL_ESC
    :   '\\' ('0'..'3') ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7')
    ;

fragment
HEX_DIGIT : ('0'..'9'|'a'..'f'|'A'..'F') ;

fragment
UNICODE_ESC
    :   '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
    ;

LONGINT
    :   INT ('l'|'L')  
    ;

