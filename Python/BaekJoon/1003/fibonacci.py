num = int(input())
a = []
for i in range(num):
    a.append(int(input()))

def memorize(*args):
    __cache = {} def wrapper(*args):
    if args in __cache:
        return __cache[args]
    else:
        __cache[args] = func(*args)
        return __cache[args]
    return wrapper

@memorize
def fibonacci(n, a, b):
    if n == 0:
        a += 1
        return [a, b]
    elif n == 1:
        b += 1
        return [a, b]
    else:
         A = fibonacci(n-1, a, b)
         B = fibonacci(n-2, a, b)
         ans = [A[0] + B[0], A[1] + B[1]]
         return ans

for i in a:                                                                                                                                                          ans = fibonacci(i, 0, 0)
    print(ans[0], ans[1])
