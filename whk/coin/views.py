from django.shortcuts import render
import requests
from .models import Coin
import pybithumb
import time
import datetime
import os
import csv
# Create your views here.

con_key = os.getenv('con_key')
sec_key = os.getenv('sec_key')
bithumb = pybithumb.Bithumb(con_key, sec_key)

# 초기 정보 저장
def get_bithumb_info():
    # # https://wikidocs.net/21881
    # tickers = pybithumb.get_tickers() # 거래되고 있는 코인 목록
    # while True:
        # for ticker in tickers:
        #     # price = pybithumb.get_current_price(ticker) # 각 코인의 현재 가격
        #     # print(price)
        #     # detail = pybithumb.get_market_detail(ticker) # 각 코인의 저가/고가/거래금액/거래량 튜플로 반환
        #     # print(detail)
        #     orderbook = pybithumb.get_orderbook("BTC") # 코인의 매수, 매도 현황
        #     # print(orderbook)
        #     ms = int(orderbook["timestamp"])
        #     dt = datetime.datetime.fromtimestamp(ms/1000) # 시간
        #     print(dt)
        #     bids = orderbook['bids'] # 매수 호가
        #     asks = orderbook['asks'] # 매도 호가
        #     print(bids)
        #     print(asks)
        # time.sleep(1) # 초당 1회만 반복되도록
        
    # all = pybithumb.get_current_price("ALL") # 모든 암호화폐의 가격
    # for k, v in all.items():
    #     print(k, v["buy_price"], v["sell_price"]) # 티커, 최고구매가, 최소판매가
    
    # 예외처리
    # while True:
    #     price = pybithumb.get_current_price("BTC")
    #     try:
    #         print(price)
    #     except:
    #         print("에러발생", price)
    #     time.sleep(1)
    
    
    # 내가 하던 것
    url = "https://api.bithumb.com/public/ticker/all"
    res = requests.get(url)
    json = res.json()
    coin_list = json["data"]
    # cnt = 0
    for coin, data in coin_list.items():
        if coin != "date":
            name = Coin.objects.get_or_create(name = coin)
            # print(name[0])
            # print(data["buy_price"])
            # print(data[0])
            name[0].check_price = data["buy_price"]
            name[0].complete_price = data["buy_price"]
            name[0].max_price = data["buy_price"]
            name[0].save()
    #         # cnt += 1
    # # print(cnt)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# --------------------------------------------------------------------

# 구입 및 판매할 때마다 갱신
def refresh():
    url = "https://api.bithumb.com/public/ticker/all"
    res = requests.get(url)
    json = res.json()
    coin_list = json["data"]
    for coin, data in coin_list.items():
        if coin != "date":
            name = Coin.objects.get_or_create(name = coin)
            name[0].check_price = data["buy_price"]
            name[0].save()
    
# 거래할 때마다 csv 파일에 내용 저장
def trade_book(date, ticker, price, trade_info):
    f = open("data.csv", "w", encoding="utf-8", newline="")
    wr = csv.writer(f)
    wr.writerow([date, ticker, price, trade_info])
    f.close()

# list에 담고, 해당 티커만 거래하도록


# 60분 마다 한 번씩 갱신시키자
def auto_sys():
    con_key = os.getenv('con_key')
    sec_key = os.getenv('sec_key')
    bithumb = pybithumb.Bithumb(con_key, sec_key)
    
    all = pybithumb.get_current_price("ALL")
    print(all)
    
    
    refresh_time = 0

auto_sys()

def list(request):
    auto_sys()
    
    coins = Coin.objects.all()
    return render(request, 'bithumb/list.html', {"coins":coins})
# ---------------------------------------------


























# # ver 1.0.
# def list(request):
#     now = datetime.datetime.now()
#     print(now)
#     con_key = os.getenv('con_key')
#     sec_key = os.getenv('sec_key')
#     bithumb = pybithumb.Bithumb(con_key, sec_key)
    
    
    # get_bithumb_info()
    # refresh()
    # while True:
        # try:
        #     all = pybithumb.get_current_price("ALL")
        #     for k, v in all.items():
        #         coin = Coin.objects.get(coin_name=k)
                
        #         # 1% 상승했으니까, 코인을 구매하고 저장하자
        #         if v["buy_price"] >= coin.coin_buy_price*1.01:
        #             coin.coin_buy_price = v["buy_price"]
        #             coin.save()
                    
        #         # 최고가 대비 1% 하락했으니까, 코인을 팔고 저장하자
        #         elif v["sell_price"] <= coin.coin_buy_price*0.99:
        #             pass
        # except:
        #     print("에러발생")
        # time.sleep(1)

    # while True:
    #     print("작동중", end=" ")
    #     print(datetime.datetime.now())
    #     try:
    #         all = pybithumb.get_current_price("ALL")
    #         # print(bithumb)
    #         krw = bithumb.get_balance("BTC")[2] # 계속 오류가 뜨네
    #         # print(f"왜 오류가? {krw}")
    #         for k, v in all.items():
    #             coin = Coin.objects.get(name=k)
    #             # print(coin.max_price)
    #             # print(type(v["buy_price"]))
    
    #             # 1% 상승했으니까, 코인을 구매하고 저장
    #             if float(v["buy_price"]) >= coin.check_price*1.01 and float(v["buy_price"]) > 2 and krw > 10000:
    #                 # 매수 
    #                 # print(krw)
    #                 orderbook = pybithumb.get_orderbook(k)
    #                 asks = orderbook['asks']
    #                 sell_price = asks[0]['price']
    #                 # print(sell_price)
    #                 unit = krw/float(sell_price)
    #                 order = bithumb.buy_market_order(k, unit)
    #                 # print(f"order : {order}")
    #                 coin.complete_price = float(v["buy_price"])
    #                 refresh()
    #                 coin.check_price = float(v["buy_price"])
    #                 coin.save()
    #                 print("매수 완료")
        
    #             # 코인을 구매한 후
    #             if coin.complete_price != 0:
    #                 # 코인의 최댓값을 저장한다.(나중에 되팔때를 대비)
    #                 if coin.max_price < float(v["buy_price"]):
    #                     coin.max_price = float(v["buy_price"])
    #                     coin.save()
    #                 # print(coin.name, end=" ")
    #                 # print(coin.complete_price)    
    #                 # 구입가 대비 1% 하락하거나, 5% 상승하거나, 최대가격 대비 1% 하락하면 코인을 팔고 저장
    #                 if float(v["sell_price"]) <= coin.complete_price*0.99 or float(v["sell_price"]) >= coin.complete_price*1.05 or float(v["sell_price"]) <= coin.max_price*0.99:
    #                     # 매도
    #                     unit = bithumb.get_balance(k)[0]
    #                     # print(f"unit : {unit}")
    #                     order = bithumb.sell_market_order(k, unit)
                        
    #                     coin.complete_price = 0
    #                     coin.max_price = 0
    #                     refresh()
    #                     coin.check_price = float(v["buy_price"])
    #                     coin.save()
                        
    #                     print("매도 완료")
    #     except:
    #         print("에러발생")
    #     time.sleep(2)

    # # 나중에 할 것
    # # 분산투자 어떻게 할 것인지?
    # # 기존에 있던 코인은 어떻게 할 것인지?

    # coins = Coin.objects.all()
    # return render(request, 'bithumb/list.html', {'coins':coins})
    
