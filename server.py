import time
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {'success': True, 'msg': '请访问/sleep/{num}页面。'}


@app.get('/sleep/{num}')
def sleep(num: int):
    time.sleep(num)
    return {'success': True, 'msg': f'等待时间: {num}秒。'}