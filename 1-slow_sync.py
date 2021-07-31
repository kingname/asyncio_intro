import time
import requests


def run_test():
    resp1 = requests.get('http://127.0.0.1:8000/sleep/3').json()
    print(resp1)
    resp1 = requests.get('http://127.0.0.1:8000/sleep/5').json()
    print(resp1)
    resp1 = requests.get('http://127.0.0.1:8000/sleep/8').json()
    print(resp1)


start = time.time()
run_test()
end = time.time()

print(f'请求3个页面，总共耗时：{end - start}')