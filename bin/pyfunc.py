import os
import sys
import antlr3
import inspect, importlib

from PyFuncLexer import PyFuncLexer
from PyFuncParser import PyFuncParser

from splunk import Intersplunk as si

import utils

logger = utils.setup_logging("pyfunc")


def parse_func(pfunc):
    char_stream = antlr3.ANTLRStringStream(pfunc)
    lexer = PyFuncLexer(char_stream)
    tokens = antlr3.CommonTokenStream(lexer)
    tokens.fillBuffer()
    parser = PyFuncParser(tokens)
    return parser.pyfunc()
    
def find_func(func):
    pkg = '.'.join(func.packages)
    module = importlib.import_module(pkg)
    members = inspect.getmembers(module)
    flist = [f for n, f in members if inspect.isfunction(f) and n==func.name]

    if len(flist)>=1: return flist[0]
    raise Exception('Cannot find the function "%s"!' % func)
    
def parse_arguments(arguments, **data):
    args = []
    for t, n in arguments:
        
        if t=='var':
            args.append(data.get(n, None))
        elif t=='numeric':
            args.append(float(n))
        elif t=='string':
            args.append(n.lstrip('"').rstrip('"'))
    
    return args

def run_func(func, **data):
    logger.debug("func.arguments=%s" % func.arguments)
    f = find_func(func)
    try:
        if len(func.arguments)==0:
            rf = f()
        else:
            args = parse_arguments(func.arguments, **data)
            logger.debug("func.arguments=%s, args=%s" % (func.arguments, args))
            rf = f(*tuple(args))
    except Exception as ex:
        logger.critical("remote call function failed. ex = %s" % ex)
        print "%s" % ex
        rf = ex
        
    return rf


if __name__ == '__main__':
    
    stdin = None
    if not os.isatty(0):
        stdin = sys.stdin

    settings = dict()
    records = si.readResults(settings = settings, has_header = True)
    sessionKey = settings['sessionKey']


    for i in range(1, len(sys.argv)):
        logger.debug("query = %s" % sys.argv[i])
        func = parse_func(sys.argv[i])
        logger.debug("func arguments = %s" % func.arguments)
        
        for rec in records:
            # it is good pratice to always pass sessionKey to functions
            rf = run_func (func, sessionKey=sessionKey, **rec)
            
            if isinstance(rf, dict):
                rec.update(rf)
            else:
                nm = func.alias if func.alias!=None else func.name
                rec.update({nm:rf})

    si.outputResults(records)
 
