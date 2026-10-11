def double(x):
    return x * 2

def add_three(x):
    return x + 3

# Compose them manually
result = add_three(double(5))  # double first, then add_three
print(result)  # 13
def compose(f, g):
    return lambda x: f(g(x))

double_then_add = compose(add_three, double)
print(double_then_add(5))  # 13