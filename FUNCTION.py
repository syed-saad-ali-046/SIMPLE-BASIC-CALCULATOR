VALUE1=input('PLEASE ENTER YOUR 1ST VALUE:')
VALUE2=input('PLEASE ENTER YOUR 2ND VALUE:')
OPREATOR=input('PLEASE MENTION YOUR OPREATOR:')
def MULTIPILICATION():
    print(float(VALUE1)*float(VALUE2))
def SUBTRACTION():
    print(float(VALUE1)-float(VALUE2))
def ADDITION():
    print(float(VALUE1)+float(VALUE2))
def DIVISION():
    print(float(VALUE1)/float(VALUE2))
if OPREATOR== '*':
    MULTIPILICATION()
elif OPREATOR== '-':
    SUBTRACTION()
elif OPREATOR== '+':
    ADDITION()
elif OPREATOR== '/':
    DIVISION()
else:
    print('SYNTAX ERROR')