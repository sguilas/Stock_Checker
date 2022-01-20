# Stock_Checker
Best Buy Stock Checker for PS5 and Xbox

I used Python with Beautifulsoup to scrape the HTML of Best Buy product pages to check the stock of PS5s and Xbox Series Consoles.
Since PS5s and Xboxes are still hard to come around, I wondered whether I could make something that can check its availability without going to the product pages themselves and manually refreshing the pages to see if they are in stock.
This uses Beautifulsoup to check whether the "Add to Cart Button" says "Add to Cart" of "Sold Out". If it's sold out then the program prints its sold out along with the date and time. If its in stock then it opens a browser tab or window to the product page.
It wont automatically buy it for you. You have to add it to your cart yourself. Why? I didn't want to make a scalping bot.

It only works for Best Buy product pages. Also it probably won't work with combos.

#### HOW TO USE ####

You will need python and Beautifulsoup installed. The program will run off the terminal.

It will ask how many you want to track.

Then it will ask for your User Agent. Just enter "my user agent" on google then copy and paste it in the terminal.

Enter what you want to track. This will act as a key in a dictionary. Then paste the url.

I"ve checked and it works on other Best Buy pages. (Doesn't work on phones. Will figure out why and fix.)

If you want to change how often it checks the product pages then just change the "Often" variable.

####

Eventually,

I'd like to be able to add support for other websites like Amazon.


Instead of running in the terminal, have it run as a desktop app.
