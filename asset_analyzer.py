from web_scraper import WebScraper
class AssetAnalyzer:
    def __init__(self):
        self.web_scraper = WebScraper()


    def analyze_ticker(self, ticker):
        trading_view_results = self.web_scraper.get_trading_view_data(ticker)
        #investing_results = self.web_scraper.get_investing_data(ticker)
        #market_sentiment = self.web_scraper.get_sentiment(ticker)
        analysis = f"Tohle je analyza tickeru {ticker} \n {trading_view_results} \n"
        return analysis
    #

    def analyze_trending(self, major_assets):
        trending_assets = []
        for asset in major_assets:
            analysis_results = self.analyze_ticker(asset)
            if analysis_results.percentage > 75:
                trending_assets.append({asset, analysis_results})