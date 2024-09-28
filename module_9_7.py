def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        for i in range(2, result):
            if result % i == 0:
                print("Составное")
                break
            else:
                print("Простое")
                break
    return wrapper

@is_prime
def sum_three(a, b, c):
    result = a + b + c
    print(result)
    return result


result = sum_three(2, 3, 6)
print(result)