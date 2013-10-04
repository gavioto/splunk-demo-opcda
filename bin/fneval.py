import os,sys,collections
import splunk.Intersplunk as si
import pyfunc as py

import utils

logger = utils.setup_logging("fneval")

def get_inputs(records, args):
    recs = []
    for t,n in args:
        if t=="var":
            recs.append([rec[n] for rec in records])
        elif t=='numeric':
            recs.append(float(n))
        elif t=='string':
            recs.append(n.lstrip('"').rstrip('"'))
            
    return recs 

if __name__ == '__main__':
    
    stdin = None
    if not os.isatty(0):
        stdin = sys.stdin

    settings = dict()
    records = si.readResults(settings = settings, has_header = True)
    sessionKey = settings['sessionKey']

    logger.debug("sessionKey = %s" % sessionKey)    
    ret = collections.OrderedDict()
    
    for i in range(1, len(sys.argv)):
        func = py.parse_func(sys.argv[i])
        logger.debug("func = %s" % func)    
        recs = get_inputs(records, func.arguments)
        logger.debug("get_inputs = %s" % recs)    
        
        f = py.find_func(func)
        f._sessionKey_ = sessionKey
        try:
            if len(func.arguments)==0:
                rf = f()
            else:
                rf = f(*tuple(recs))
        except Exception as ex:
            logger.critical("fneval: ex = %s" % ex)
            print "%s" % ex
            rf = ex
            
        logger.debug("rf = %s" % rf)
        
        nm = func.name
        if func.alias!=None: nm = func.alias
        ret[nm] = rf

    logger.debug("ret = %s" % ret)
    logger.debug("records = %s" % records)
    

    si.outputResults([ret])
    
