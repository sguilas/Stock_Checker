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
urls = {}
often = 15
flag = True
times = int(input("Enter how many URLs you will track: "))
i=0
while times!=0:
    prod_name = str(input("What you are tracking: "))
    prod_url = str(input("URL: "))
    urls[prod_name] = prod_url
    times-=1

#user = user()
#ps5 = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
#ps5_dig = "https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161"
#xbox_x = "https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324"
#xbox_s = "https://www.bestbuy.com/site/microsoft-xbox-series-s-512-gb-all-digital-console-disc-free-gaming-white/6430277.p?skuId=6430277"

while flag == True:
    now = datetime.datetime.now()
    real_time = now.strftime("%d/%m/%Y %H:%M:%S")
    for key, url in urls.items():
        print("################################################")
        print(f"For {key} (Best Buy):")
        ans = all(user,url)
        if ans == True:
            webbrowser.open(url)
            flag = False
            break
        else:
            print(f"It's still sold out as of {real_time}\n")

    time.sleep(often)