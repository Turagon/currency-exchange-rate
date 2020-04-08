import requests 
import json
import time 

url = 'https://tw.rter.info/capi.php'
r = requests.get(url)
ex_rate = json.loads(r.text)
currency_name = {"台幣" : "TWD", "美金" : "USD", "歐元" : "EUR", "日圓" : "JPY", \
"港幣" : "HKD", "英鎊" : "GBP", "人民幣" : "CNY", "韓元" : "KRW", "澳幣" : "AUD", \
"紐西蘭幣" : "NZD", "新加坡幣" : "SGD", "泰銖" : "THB", "加幣" : "CAD", "印度盧比" : "INR", \
"瑞士法郎" : "CHF"}


def USD(content, origin_c, target_c) :
    origin_ce = currency_name[origin_c]
    target_ce = currency_name[target_c]
    if origin_c == "美金" :
        print("本日", origin_c, "對", target_c, "是", ex_rate[(origin_ce+target_ce)]["Exrate"])
    else :
        origin_rate = ex_rate["USD" + origin_ce]["Exrate"]
        target_rate = ex_rate["USD" + target_ce]["Exrate"]
        time_rate = ex_rate["USD" + target_ce]["UTC"]
        exchange_rate = round(float(target_rate)/float(origin_rate), 4)
        print("本日", origin_c, "對", target_c, "是", exchange_rate)
        print(time_rate) 

def main() :
    origin_c = input("請輸入本幣幣別 : ")
    target_c = input("請輸入兌換幣別 : ")
    USD(ex_rate, origin_c, target_c)
    print("本資料引自即匯站")

main()



