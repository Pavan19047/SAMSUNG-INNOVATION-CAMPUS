# n = 5  
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))

# for i in range(n - 2, -1, -1):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))

# pattern = [1, 3, 5, 9, 5, 3, 1]
# max_width = max(pattern)
# for num in pattern:
#     spaces = (max_width - num) // 2
#     print(' ' * spaces + '*' * num)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# print(f'Factorial {factorial(5)}')


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# print(f'Fibonacci {fibonacci(5)}')

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# print(f'Is  prime: {prime(5)}')

a = 10
b = 8

# print(f'Left Shift: {b << 2}')  
# print(f'Right Shift: {b >> 3}') 
# print(f'Bitwise AND: {a & b}')  
# print(f'Bitwise OR: {a | b}')   
# print(f'Bitwise XOR: {a ^ b}')  
# print(f'Bitwise NOT: {~a}')  


def greatest_of_three(a, b, c): #without logical operators
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(f'Greatest of three: {greatest_of_three(10, 20, 30)}')