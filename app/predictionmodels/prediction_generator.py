import matplotlib.pyplot as plt
import pandas as pd

from app.predictionmodels.sarimax import Sarimax


class PredictionGenerator:

    division_factor = 0.66

    def transform(self, paths):

        for datapath in paths:
            df = pd.DataFrame(list(datapath.historical_marketshares.items()), columns=['month', datapath.handset]).sort_values(by=['month'])

            # create train and test set

            size = int(len(df) * self.division_factor)
            train, test = df[0:size], df[(size-1):len(df)]

            # aggregate the dataset at monthly level

            df.Timestamp = pd.to_datetime(df['month'], format='%Y-%m')
            df.index = df.Timestamp
            df = df.resample('M').mean()

            train.Timestamp = pd.to_datetime(train['month'], format='%Y-%m')
            train.index = train.Timestamp
            train = train.resample('M').mean()

            test.Timestamp = pd.to_datetime(test['month'], format='%Y-%m')
            test.index = test.Timestamp
            test = test.resample('M').mean()

            # future_shares = {
            #     '2019-01': 0.0,
            #     '2019-02': 0.0,
            #     '2019-03': 0.0,
            #     '2019-04': 0.0,
            #     '2019-05': 0.0,
            #     '2019-06': 0.0
            # }

            # future = pd.DataFrame(future_shares.items(), columns=['month', 'marketshare']).sort_values(by=['month'])
            # future.Timestamp = pd.to_datetime(future['month'], format='%Y-%m')
            # future.index = future.Timestamp
            # future = future.resample('M').mean()

            # test = test.append(future)

            ARIMA_order = (5, 1, 0)
            ARIMA_disp=0
            # predicted = Arima().predict(train, test, ARIMA_order, ARIMA_disp)
            predicted = Sarimax().predict(df)

            # ARIMA_order = (3, 1, 0)
            # ARIMA_disp=0
            # predicted_2 = Arima().predict(train, test, future, ARIMA_order, ARIMA_disp)

            # train.marketshare.plot()
            # test.marketshare.plot()
            predicted.marketshare.plot()
            # predicted_2.marketshare.plot()
            # print('MSE:', mean_squared_error(predicted.values, test.values))


            plt.show(block=True)

