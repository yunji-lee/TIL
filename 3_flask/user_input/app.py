from flask import Flask, render_template, request
# request를 몰래 처리하다가 import함으로 가시화
from iexfinance.stocks import Stock

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_stock')
def stock():
    return render_template(
        'search_stock.html'
        is_first_search=True,
    )


@app.route('/search_result')
def result():
    TOKEN = 'pk_77de0489d51e4cefa8eddf6c8f182c2b'

    user_input = request.args.get('keyword') # dic[]형태가 아닌 .get 을 쓰는건 값이 없을 때 에러나지 않게 하는 것
    if user_input:
        stock = Stock(user_input, token=TOKEN) # 대문자로 시작하면 클래스
    else:
        return render_template(
            'search_stock.html',
            is_success = False,
        )

    try :
        data = stock.get_quote()
    except:
        return render_template(
            'search_result.html',
            is_success=False,
        )

    return render_template(
        'search_result.html',
        is_success=True,
        c_name=data['companyName'],
        l_price=data['latestPrice'],
    )


if __name__ == '__main__':
    app.run(debug=True)