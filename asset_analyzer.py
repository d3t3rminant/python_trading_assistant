from web_scraper import WebScraper
class AssetAnalyzer:
    def __init__(self):
        self.web_scraper = WebScraper()


    def analyze_ticker(self, ticker):
        print("Retrieving data from trading view")
        #trading_view_results = self.web_scraper.get_trading_view_data(ticker)
        print("Retrieving data from investing.com")

        #investing_results = self.web_scraper.get_investing_data(ticker)
        #print("Retrieving market sentiment")

        market_sentiment = self.web_scraper.get_sentiment(ticker)
        analysis = f"This is analysis of {ticker} \n {market_sentiment} \n"
        return analysis


    def analyze_trending(self, major_assets):
        trending_assets = []
        for asset in major_assets:
            analysis_results = self.analyze_ticker(asset)
            if analysis_results.percentage > 75:
                trending_assets.append({asset, analysis_results})