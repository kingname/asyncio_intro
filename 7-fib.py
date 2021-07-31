import time


def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


start = time.time()
result = fib(36)
end = time.time()

print(f'计算斐波拉契数列第36项，耗时：{end - start}')