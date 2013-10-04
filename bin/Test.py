import inspect
import importlib
from PyFuncParser import Function


def find_func(func):
    module = 'pyfunc'  # default module
    
    if len(func.packages)>0:
        pkg = '.'.join(func.packages)
        module = importlib.import_module(pkg)
        
    members = inspect.getmembers(module)
    flist = [o for o in members if inspect.isfunction(o[1]) and o[0]==func.name]
    
    if len(flist)>=1: return flist[0][1]
    raise Exception('Cannot find the function "%s"!' % func)
    
def parse_arguments(arguments, **data):
    args = []
    for arg in arguments:
        if arg[0]=='var':
            args.append(data.get(arg[1], None))
        elif arg[0]=='numeric':
            args.append(float(arg[1]))
        elif arg[0]=='string':
            args.append(arg[1])
            
    return args
    

def run_func(func, **data):
    f = find_func(func)
    
    if len(func.arguments)==0:
        rf = f()
    else:
        args = parse_arguments(func.arguments, **data)
        rf = f(*tuple(args))

    return rf

def test1():
    func = Function()
    func.packages = ['aes']
    func.name = 'EncryptRunner'
    func.arguments = [('var', 'host')]
    data = dict(host='1234567890')
    
    rf = run_func(func, **data)
    print "%s\n" % rf

    dfunc = Function()
    dfunc.packages = ['aes']
    dfunc.name = 'DecryptRunner'
    dfunc.arguments = [('var', 'encrypted')]

    print "%s\n" % run_func(dfunc, encrypted=rf)

def test2():
    import pyfunc
    s1 = "aes.EncryptRunner(Species) as Encrypted" 
    s2 = "aes.DecryptRunner(Encrypted) as Origin"
    
    f1 = pyfunc.parse_func(s1)
    f2 = pyfunc.parse_func(s2)
    
    print "%s\n" % f1.packages
    print "%s\n" % f1.name
    
    # print "%s\n" % f2.packages
    
if __name__ == '__main__':
    test2()