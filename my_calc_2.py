def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("oga u nor go primary school ? ")
    return a/b 

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        raise ValueError("Nawa you fit divide by 0?")
    return a % b

OPERATOR  = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiply,
    "/" : division,
    "^" : power,
    "%" : modulus,
}

def get_number(number):
    while True:
        try:
            return(float(input(number)))
        except ValueError:
            print("\n wrong value try again.\n")

def get_operator():
    while True:
        sign = list(OPERATOR.keys())
        op =input(f"operator {sign} :").strip()
        if op in OPERATOR:
            return op
        print("Not a valid operator try again?")

def show_history(history):
    if not history:
        print(" No calculation yet")
        return

    print("calculation history")
    for i, entry in enumerate(history, 1):
        print(f"{i}. {entry}")

print()

def main():
    print("=" * 45)
    print("THIS IS MY FIRST CLI CALCULATOR")
    print("=" * 45)
    
    History = []

    while True:
        
        Command = input("type Enter to calculate, Exit/Quit to Terminate calculator or History to View History :")

        if Command == "exit":
            print("good boy")
            break

        if Command == "History":
            show_history(History)
            continue

        num1 = get_number("First number : ")
        op = get_operator()
        num2 = get_number("second number : ")

        try:
            result = OPERATOR[op](num1, num2)
        except ValueError as e :
                print(f"\n error {e}" )
                continue

        def fmt(n):
            if n == int(n): 
                return int(n)
            else: 
                return round(n, 10)

        Expression = f"{fmt(num1)} {op} {fmt(num2)} = {fmt(result)}"

        print(f"\n result : {Expression} \n")
        
        History.append(Expression)

if __name__ == "__main__":
    main()
    