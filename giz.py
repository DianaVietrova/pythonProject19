def safe_calculator(func):
    def wrapper(expression):
        try:
            restricted_globals = {'__builtins__': None}
            result = eval(expression, restricted_globals, {})
            return result
        except Exception as e:
            print(f"Error in calculation: {e}")
            return None
    return wrapper


@safe_calculator
def calculate(expression):
    return eval(expression)

result = calculate("45 + 39")
print("результат:", result)

result = calculate("67 / 0")
print("результат:", result)

