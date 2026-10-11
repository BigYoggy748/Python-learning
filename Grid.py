def Row_type1():
    print('+ - - - - + - - - - +')

def Row_type2():
    print('|         |         |')

def grid_placement():
    Row_type1()
    Row_type2() 
    Row_type2()
    Row_type2()
    Row_type2()
    Row_type1()
    Row_type2()
    Row_type2()
    Row_type2()
    Row_type2()
    Row_type1()
grid_placement()

#Better way of doing it using loop
def Row_type1():
    print('+---- +---- +')

def Row_type2():
    print('|     |     |')

def draw_row(f, times):
    for i in range(times):
        f()

def grid_placement():
    draw_row(Row_type1, 1)
    draw_row(Row_type2, 4)
    draw_row(Row_type1, 1)
    draw_row(Row_type2, 4)
    draw_row(Row_type1, 1)

grid_placement()