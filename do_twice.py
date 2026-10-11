def print_yotan():
    print('YOTAN')


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

#│
#├── do_twice runs (1st time)
#│    ├── print_twice runs → spam
#│    │                    → spam
#│    │
#│    └── print_twice runs → spam
#│                         → spam
#│
#└── do_twice runs (2nd time)
  #  ├── print_twice runs → spam
    #│                    → spam
    #│
    #└── print_twice runs → spam
    #                     → spam