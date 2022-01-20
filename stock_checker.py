import webbrowser
from bs4 import BeautifulSoup
import requests
import datetime
import time

def user():
    headers = {"User-Agent":""}
    agent = input("Google 'my user agent' and paste the result here:")
    headers["User-Agent"] = agent
    return headers

def get_status(user,url):
    r = requests.get(url, headers = user)
    soup = BeautifulSoup(r.text, "html.parser")
    status = soup.find("div", {"class":"fulfillment-add-to-cart-button"}).text
    return status

def out_or_no(status,time,url):
    if "Add to Cart" in status:
        return True
    elif "Sold Out" or "Unavailable nearby" in status:
        return False

def all(user, url):
    url = url
    status = get_status(user,url)
    return out_or_no(status,time,url)


print(f"This checks the PS5 and Xbox Series Product pages whether they are in stock by parsing through the HTMl.\n")
print(f"If it's in stock it will open the webpage so you could buy it and stop the loop.\n")

user = user()
ps5 = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
ps5_dig = "https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161"
xbox_x = "https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324"
xbox_s = "https://www.bestbuy.com/site/microsoft-xbox-series-s-512-gb-all-digital-console-disc-free-gaming-white/6430277.p?skuId=6430277"
often = 15

while True:
    now = datetime.datetime.now()
    real_time = now.strftime("%d/%m/%Y %H:%M:%S")
    print("################################################")
    print("For PS5 (Best Buy):")
    ans_ps5 = all(user,ps5)
    if ans_ps5==True:
        webbrowser.open(ps5)
        break
    else:
        print(f"It's still sold out as of {real_time}\n")
    print("For PS5 (Digital) (Best Buy):")
    ans_ps5D = all(user,ps5_dig)
    if ans_ps5D==True:
        webbrowser.open(ps5_dig)
        break
    else:
        print(f"It's still sold out as of {real_time}\n")
    print("For Xbox Series X (Best Buy):")
    ans_Xbx = all(user,xbox_x)
    if ans_Xbx==True:
        webbrowser.open(xbox_x)
        break
    else:
        print(f"It's still sold out as of {real_time}\n")
    print("For Xbox Series S (Best Buy):")
    ans_Xbs = all(user,xbox_s)
    if ans_Xbs==True:
        webbrowser.open(xbox_s)
        break
    else:
        print(f"It's still sold out as of {real_time}\n")
        print("################################################")
    time.sleep(often)