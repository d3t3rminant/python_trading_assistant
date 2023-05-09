class Constants:

    __TRADING_VIEW_TIME_FRAMES = ['5m', '15m', '1h', '4h', '1D', '1W']

    __INVESTING_TIME_FRAMES_MAP = {
        '300':'5M',
        '900': '15M',
        '3600': '1H',
        '18000': '5H',
        '86400': '1D',
        'week': '1W'
    }

    @property
    def trading_view_time_frames(self):
        return self.__TRADING_VIEW_TIME_FRAMES

    @property
    def investing_time_frames_map(self):
        return self.__INVESTING_TIME_FRAMES_MAP