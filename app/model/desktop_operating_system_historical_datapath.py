import pandas as pd

class DesktopOperatingSystemHistoricalDatapath:

    def __init__(self, historical_marketshares, os, country):
        self.os = os
        self.historical_marketshares = historical_marketshares
        self.country = country

    def as_datapath(self):
        return pd.DataFrame(list(self.historical_marketshares.items()),
                            columns=['month', 'marketshare']).sort_values(
            by=['month'])

