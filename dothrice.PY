def do_thrice(f, bruce):

    f(bruce)

    f(bruce)

    f(bruce)



def print_thrice(bruce):

    print(bruce)

    print(bruce)

    print(bruce)



def do_six(f, bruce):

    do_thrice(f, bruce)

    do_thrice(f, bruce)

    do_thrice(f, bruce)



# Correct: no () — you store the function itself, then call it when you want.

multiply = do_six

multiply(print_thrice, 'YOGGY')