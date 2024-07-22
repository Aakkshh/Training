def generate_fibonacci(terms):
    fibonacci_series = []
    
    a, b = 0, 1
    
    for _ in range(terms):
        fibonacci_series.append(a)
        a, b = b, a + b
         
    return fibonacci_series


terms = 5
print(generate_fibonacci(terms))
