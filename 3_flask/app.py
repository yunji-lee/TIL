from flask import Flask, render_template
import random

print(__name__) # __name__ 은 스트링이 들어있는 변수다
app = Flask(__name__)


@app.route('/')  # 주소 뒤에 /(슬래시)가 있으면 함수를 실행해라
def index():
    return render_template('index.html')


@app.route('/lotto')
def lotto():
    lucky_numbers = random.sample(range(1, 46), 6)
    return f'{lucky_numbers}'


@app.route('/pick_lotto')
def pick_lotto():
    lucky_numbers = random.sample(range(1, 46), 6)
    #print(sorted(lucky_numbers)) # return만 바뀌고 원본은 그대로
    lucky_numbers.sort() # return이 바뀌는 것이 아니라 정렬시켜서 저장. 즉 원본 변경
    return render_template('pick_lotto.html', numbers=lucky_numbers)


@app.route('/lotto/<int:num>') # variable routing의 상징적인 기호
def lotto(num):
    lucky_numbers = random.sample(range(1, 46), 6)
    lucky_numbers.sort()

    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    res = requests.get(url).text  # type이 str
    data = json.loads(res)  # type이 dict가 됨

    real_numbers = []
    if data['returnValue'] == 'success':
        for key, value in data.items():
            if 'drwtNo' in key:
                real_numbers.append(value)
            # print(key, value)
        real_numbers.sort()
    # real_numbers => 실제 로또 번호 / luck_numbers => 지정한 로또번호

import requests
import json
@app.route('/get_lotto/<int:num>')
def get_lotto(num):
    #회차별 번호를 가져오는 것을 직접 써보자
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    res = requests.get(url).text # type이 str
    data = json.loads(res) # type이 dict가 됨

    real_numbers = []
    if data['returnValue'] == 'success':
        for key, value in data.items():
            if 'drwtNo' in key:
                real_numbers.append(value)
            # print(key, value)
        real_numbers.sort()

    return render_template('get_lotto.html', numbers=real_numbers, drawo_no=num)


if __name__ == '__main__':
    app.run(debug=True) # 위의 일련의 과정이 웹개발의 본질

#localhost는 무슨 의미인가?

