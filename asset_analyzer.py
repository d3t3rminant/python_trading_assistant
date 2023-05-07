from web_scraper import WebScraper
class AssetAnalyzer:
    def __init__(self):
        self.web_scraper = WebScraper()


    def analyze_ticker(self, ticker):
        analysis_data = {}

        print("Retrieving data from Trading View, hold on...")
        analysis_data['trading_view'] = self.web_scraper.get_trading_view_data(ticker)

        print("Retrieving data from investing.com, just a second...")
        analysis_data['investing'] = self.web_scraper.get_investing_data(ticker)

        print("Retrieving market sentiment, almost done...")
        analysis_data['sentiment'] = self.web_scraper.get_sentiment(ticker)
        return analysis_data


    def analyze_trending(self, major_assets):
        trending_assets = []
        for asset in major_assets:
            analysis_results = self.analyze_ticker(asset)
            if analysis_results.percentage > 75:
                trending_assets.append({asset, analysis_results})