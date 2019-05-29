flask란?
* 파이썬 기반으로 웹 어플리케이션을 구현하는 프레임 워크 툴
* 장고와의 차이점을 보자, 장고를 사용할 때 이해를 돕고자 플라스크를 공부함

TIL에 3_flask 폴더 생성

cd 3_flask

pip install flask

3_flask에 touch app.py

app.py에 작성

```python
from flask import Flask

print(__name__) # __name__ 은 스트링이 들어있는 변수다
app = Flask(__name__)


@app.route('/')
def index():
    return  '안녕하세요'


if __name__ == '__main__':
    app.run(debug=True)
```

터미널에서

python app.py 입력

이후 주소를 컨트롤 + 클릭

----

## flask학습의 핵심

client가 보낸 요청을 'server가 처리하는 일련의 행동'을 보면

0. 요청 request
1. 주문서확인, URL분석
2. 함수실행 , action
3. html로 출력
4. 문서를 내보낸다