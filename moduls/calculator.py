import subtraction, addition, division, multiplication

def calculate(a, b, operation):
    if  operation == 'addition':
        return addition.operate(a, b)
    elif  operation == 'subtraction':
        return subtraction.operate(a, b)
    elif operation == 'multiplication':
        return multiplication.operate(a, b)
    elif operation == 'division':
        return division.operate(a, b)
