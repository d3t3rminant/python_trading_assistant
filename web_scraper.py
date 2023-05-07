import time

import selenium.common.exceptions
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

            """chrome_options.add_argument('--headless')
            chrome_options.add_argument('window-size=1200,1100');
            self.driver = webdriver.Chrome(options=chrome_options)"""

            # For debugging purposes -> to see how selenium interacts on the screen ↓
            chrome_options2 = Options()
            chrome_options2.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(options=chrome_options2)

    def close_browser(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
    @staticmethod
    def format_ticker_for_investing(input_str):
        if len(input_str) == 6:
            return input_str[:3].lower() + '-' + input_str[3:].lower()
        else:
            raise ValueError("Input string must be 6 characters long")

    def get_trading_view_data(self, ticker):
        trend_results = {}
        self.open_browser() # Open browser window
        try:
            #Open tradinview.com with a specific ticker to analyse ↓
            self.driver.get(f"https://www.tradingview.com/symbols/{ticker}/technicals/?exchange=FX")



            for time_frame in self.constants.trading_view_time_frames: # TODO: Change for tf locators/ids
                button_tf = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, time_frame)))

                button_tf.click()

                # In case my code breaks down, this worked :) ↓
                #time.sleep(1)  # Necessary in order to wait for the right class assignment.
                #div_container = self.driver.find_element(By.CLASS_NAME, "summary-kg4MJrFB")


                div_container = WebDriverWait(self.driver, 5)\
                    .until(EC.presence_of_element_located((By.CLASS_NAME, "summary-kg4MJrFB")))

                # Necessary for JS to display accurate info in "summary" section
                WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_any_elements_located(
                       (By.CSS_SELECTOR, '[class*=strong-sell], '
                                         '[class*=sell-], '
                                         '[class*=buy-], '
                                         '[class*=neutral-], '
                                         '[class*=strong-buy-]' )
                    )
                )
                time.sleep(0.5) # necessary for my sluggish internet to load the correct info lol
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
        except TimeoutError:
            return None
        self.close_browser()
        return trend_results
        # TODO: Update exceptions and test it
        # TODO: Add exception if not known ticker is entered and page is not found



    def get_investing_data(self, ticker):
        trend_results = {}
        self.open_browser()  # Open browser window

        try:
            #Open investing.com with a specific ticker to analyse (need to format user's input first ↓)
            self.driver.get(f"https://www.investing.com/currencies/{WebScraper.format_ticker_for_investing(ticker)}-technical")

            # Consent to cookies to continue to the site ↓
            accept_cookies_button = WebDriverWait(self.driver, 5) \
                .until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            accept_cookies_button.click()

            # Contains every button to change the time frame of Technical Analysis
            buttons_container = WebDriverWait(self.driver, 3)\
                .until(EC.presence_of_element_located((By.ID, "technicalstudiesSubTabs")))




            for time_frame in self.constants.investing_time_frames_map.keys(): # dictionary of {'300':'5M'}-like pairs
                # Find button with specific TF ↓, click the button to change the TF
                button_tf = WebDriverWait(buttons_container,3)\
                    .until(EC.presence_of_element_located((By.XPATH, f"//li[@data-period='{time_frame}']")))
                button_tf.click()
                # Then the webpage starts to load technical indicators for this particular time frame period


                # Technical indicators Summary container with a single span element
                summary_container = WebDriverWait(self.driver, 3) \
                    .until(EC.visibility_of_element_located((By.CLASS_NAME, "summary")))

                # A <span> element with text containing trend direction (buy/sell etc) ↓
                technical_summary = WebDriverWait(summary_container, 3) \
                    .until(EC.presence_of_element_located((By.TAG_NAME, "span")))
                trend_results[self.constants.investing_time_frames_map[time_frame]] = technical_summary.text


        except:
            print("Unexpected error during retrieving data from investing.com ")

        finally:
            self.close_browser()

        return trend_results


    def get_sentiment(self, ticker):
        pass

