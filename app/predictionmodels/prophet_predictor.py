import pandas as pd
from fbprophet import Prophet


class ProphetPredictor:

    def predict(self, paths):
        ms_column_name = 'ds'

        dataframe = pd.DataFrame({ms_column_name: []})
        for datapath in paths:

            df = pd.DataFrame(list(datapath.historical_marketshares.items()), columns=['month', datapath.item]).sort_values(by=['month'])

            df.Timestamp = pd.to_datetime(df['month'], format='%Y-%m')
            df.index = df.Timestamp
            df = df.resample('M').mean()

            # df1 = Sarimax().predict(df)
            df1 = self.predict_single_item(datapath)[[ms_column_name, 'yhat']].copy()

            df1 = df1.rename(columns={'yhat': datapath.item})

            dataframe = dataframe.merge(df1, on=ms_column_name, how='right')

        dataframe.Timestamp = pd.to_datetime(dataframe['ds'], format='%Y-%m')
        dataframe.index = dataframe[ms_column_name]
        dataframe = dataframe.resample('M').mean()

        dataframe = dataframe.clip(lower=0.0)
        dataframe.index = dataframe.index.map(str)

        # dataframe = dataframe.loc[dataframe.index > '2018-12-31 00:00:00']

        print('dataframe', dataframe)

        return dataframe

    def predict_single_item(self, datapath):
        df = pd.DataFrame(list(datapath.historical_marketshares.items()),
                          columns=['month', datapath.item]).sort_values(by=['month'])

        # prepare the input dataframe to be used by Prophet
        df = df.rename(columns={df.columns.values.tolist()[1]: "y"})

        # df.ds = pd.to_datetime(df['month'], format='%Y-%m')
        # df.index = df.ds
        # df = df.resample('M').mean()

        df = df.rename(columns={df.columns.values.tolist()[0]: "ds"})

        m = Prophet()
        m.fit(df)

        future = m.make_future_dataframe(periods=12, freq='M')
        forecast = m.predict(future)

        # forecast = forecast[forecast['ds'].dt.day == 1]

        # fig1 = m.plot(forecast)
        # plt.show(block=True)

        return forecast