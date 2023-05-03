class Constants:
    __MAJOR_ASSETS = ['EURUSD', 'USDJPY', 'GBPUSD', 'USDCHF', 'USDCAD', 'Gold',
                     'Silver', 'Oil', 'BTCUSD', 'ETHUSD', 'US100']

    __TRADING_VIEW_TIME_FRAMES = ['4H', '1W', '1D', '1h', '5m']

    @property
    def major_assets(self):
        return self.__MAJOR_ASSETS

    @property
    def trading_view_time_frames(self):
        return self.__TRADING_VIEW_TIME_FRAMES