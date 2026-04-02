# nth Fibonacci number.
def nth_fibonacci_number(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1): # (n + 1) because of indexing starting at 0
        a, b = b, a + b
    return b

def fibonacci_series(n: int) -> list[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    series = [0, 1]
    for i in range(2, n):
        series.append(series[i - 1] + series[i - 2])
    return series

print(fibonacci_series(11))

print(nth_fibonacci_number(11)) 

