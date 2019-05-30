from iexfinance.stocks import Stock
import  pprint

pp = pprint.PrettyPrinter()

TOKEN = 'pk_77de0489d51e4cefa8eddf6c8f182c2b'

aapl = Stock('FB', token=TOKEN) # 대문자로 시작하면 클래스
#pp.pprint(aapl.get_quote())
data = aapl.get_quote()
#pp.pprint(data)
print(data['companyName'], data['latestPrice'])