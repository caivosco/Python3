
print('always executed')

def myfnc():
 print('m1 module name=%s' %(__name__))

def function_test():
 print('is a test')

if __name__=='__main__':
 print('calling myfnc()')
 myfnc()

print('last execution') 
