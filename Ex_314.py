from multiprocessing.sharedctypes import Value


def right_justify(s):
    space = 70 - len(s)
    print(' ' * space + s)
right_justify("yotan")

def do_twice(f, value):
    f(value)  
    f(value)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value) 

do_four( print_twice, 'YOTAN')