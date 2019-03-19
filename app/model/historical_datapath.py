import pandas as pd


class HistoricalDatapath():

  def __init__(self, historical_marketshares, item, country):
    self.item = item
    self.historical_marketshares = historical_marketshares
    self.country = country

  def as_datapath(self):
    return pd.DataFrame(list(self.historical_marketshares.items()), columns=['month', self.item]).sort_values(
      by=['month'])

  def serialize(self):
    return {
      'country': self.country,
      'historicalMarketshares': self.historical_marketshares,
      'desktopOperatingSystem': self.item
    }



