
### EX 15 e 16 PYTHON ###
# SÉRIE FIBONACCI #

def fibonacci(n):
    fibo = [1, 1]
    while True:
        next_value = sum(fibo[-1:-3:-1])
        
        if next_value <= n:
            fibo.append(next_value)
        else:
            return fibo

print(fibonacci(700))