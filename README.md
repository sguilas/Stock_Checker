# Stock_Checker
Best Buy Stock Checker for PS5 and Xbox

I used Python with Beautifulsoup to scrape the HTML of Best Buy product pages to check the stock of PS5s and Xbox Series Consoles.
Since PS5s and Xboxes are still hard to come around, I wondered whether I could make something that can check its availability without going to the product pages themselves and manually refreshing the pages to see if they are in stock.
This uses Beautifulsoup to check whether the "Add to Cart Button" says "Add to Cart" of "Sold Out". If it's sold out then the program prints its sold out along with the date and time. If its in stock then it opens a browser tab or window to the product page.
It wont automatically buy it for you. You have to add it to your cart yourself. Why? I didn't want to make a scalping bot.

It only works for Best Buy product pages. Also it probably won't work with combos.

#### HOW TO USE ####

It will ask for your User Agent. Just enter "my user agent" on google then copy and paste it in the terminal.

I"ve checked and it works on other Best Buy pages. (Doesn't work on phones. Will figure out why and fix.) Just copy the URL into the code.

####

Eventually...

I'd like to be able to add support for other websites like Amazon.

I plan to add a way so it asks how which urls you would like to check instead of going into the code to change them.
