class Constants:
    __MAJOR_ASSETS = ['EURUSD', 'USDJPY', 'GBPUSD', 'USDCHF', 'USDCAD', 'Gold',
                     'Silver', 'Oil', 'BTCUSD', 'ETHUSD', 'US100']

    __TRADING_VIEW_TIME_FRAMES = ['5m', '15m', '1h', '4h', '1D', '1W']

    __INVESTING_TIME_FRAMES = ['week', '86400', '18000', '3600', '300'] # 1W, 1D, 5H, 1H, 5M (in seconds)

    __AVAILABLE_TICKERS = ['EURUSD', 'USDJPY', 'AUDNZD'] # TODO: List out all available tickers
    @property
    def major_assets(self):
        return self.__MAJOR_ASSETS

    @property
    def trading_view_time_frames(self):
        return self.__TRADING_VIEW_TIME_FRAMES

    @property
    def investing_time_frames(self):
        return self.__INVESTING_TIME_FRAMES