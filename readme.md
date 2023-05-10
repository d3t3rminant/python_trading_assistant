**Introduction:**

    A simple Python app that uses Selenium to automate the process of retrieving and compiling 
    technical analysis data for a user-selected forex pair. The data is sourced from leading 
    financial analysis sites: tradingview.com, investing.com, and myfxbook.com. This app can 
    automate the manual process of searching different sites for a quick technical analysis 
    overview. The technical analysis provided consists of a summary of moving averages and 
    oscillators on various time frames from tradingview.com and investing.com, 
    followed by market sentiment from myfxbook.com


**To get started:**

1) On your device, install chrome webdriver. (Download here - https://chromedriver.chromium.org/downloads)
You don't have to add the chromedriver to the path, just copy the chromedriver.exe file into this project's folder.
Make sure you download and install a driver that suits the version of your Chrome.
How to check the version of Chrome: 
https://www.youtube.com/watch?v=49wT_RexweA

2) In case the final asset analysis results are incorrect, try to increase value of x 
in "time.sleep(x)" (in web_scraper.py methods). This solves some issues in loading content where Selenium Waits are not helpful.
Workaround to be found in version 2.0 


**How it should work:**
    https://youtu.be/JUCWksD1ahc

**Troubleshooting:**

    If the final asset analysis results are incorrect, try increasing the value of x in "time.sleep(x)" 
    in the web_scraper.py methods. This is a workaround for some issues related to content loading where 
    Selenium Waits are not effective. A more permanent solution will be implemented in version 2.0.

**Contributing:**

    Note this is my first Python app. Usually it works (90 % of the time), but has a lot of things that 
    could be improved.
    Version 2.0 will take care of it. If you have any suggestion, please let me know.  
    (Sometimes) ChatGPT is not enough :)

**Coming in Version 2.0:**

    Version 2.0. is going to be able to analyse provided list of assets (not only FX pairs) and select
    only those assets that are moving in a (strong) trend, based on given criteria - adjustable. 
    Also it will have a small web interface hosted on a local server for better clarity and readability
    of retrieved results. Hopefully I'll be able to reduce the time cost of every process. 