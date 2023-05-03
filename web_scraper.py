import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from selenium.webdriver.chrome.options import Options

class WebScraper:
    #Class Variables
    class_trends = ["strong-buy", "strong-sell", "buy", "sell", "neutral"] # css class selector in Trading View
    def __init__(self):
        self.driver = None
        self.constants = Constants()

    def open_browser(self):
        if self.driver is None:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=chrome_options)

    def close_browser(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None

    def get_trading_view_data(self, ticker):
        trend_results = {}
        self.open_browser() # Open browser window
        try:
            self.driver.get(f"https://www.tradingview.com/symbols/{ticker}/technicals/?exchange=FX")
            for time_frame in self.constants.trading_view_time_frames: # TODO: Change for tf locators/ids
                button_tf = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, time_frame)))
                button_tf.click()
                time.sleep(1)  # Necessary in order to wait for the right class assignment. TODO: Find workaround
                div_container = self.driver.find_element(By.CLASS_NAME, "summary-kg4MJrFB")
                div_summary = div_container.find_element(By.CLASS_NAME, "container-zq7XRf30")
                class_names = div_summary.get_attribute("class")

                for trend in self.class_trends:
                    if trend in class_names:
                        trend_results[time_frame] = trend
                        break
                    else:
                        trend_results[time_frame] = "Not available"
        except AttributeError:
            return None
        return trend_results

    def get_investing_data(self, ticker):
        pass

    def get_sentiment(self, ticker):
        pass

