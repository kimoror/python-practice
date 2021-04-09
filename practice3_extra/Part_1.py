from additional_module import *

# whitespace before '('.
print( 1)


# missing whitespace around operator.
print(2%2)


# missing whitespace after ','.
print(2,3)


# unexpected spaces around keyword / parameter equals.;
def foo(x = 14):


# expected 2 blank lines, found 1.
print(2)

# multiple statements on one line (colon).
if foo:print(3)


# multiple statements on one line (semicolon).
print('first'); print('second')


# comparison to None should be 'if cond is None:'.
def foo2(x):
    if x == None:
        print('Error')


# comparison to True should be 'if cond is True:' or 'if cond:'.
def foo3(x):
    if x == True:
        print('Error')


func_one()
func_three()
#func_two() can`t import