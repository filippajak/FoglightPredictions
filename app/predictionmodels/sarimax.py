import pandas as pd
import statsmodels.api as sm


class Sarimax:

    def predict(self, df):
        mod = sm.tsa.statespace.SARIMAX(df.values, order=(10, 1, 1), enforce_stationarity=False)
        results = mod.fit()

        pred = results.get_forecast(steps=10)
        pred_ci = pred.conf_int()

        forecast = pd.DataFrame(pred.predicted_mean, columns=[df.columns.tolist()[0]])

        mo = ['2018-12', '2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07', '2019-08',
              '2019-09', '2019-10']
        forecast['month'] = pd.Series(mo)

        forecast = forecast[1:]

        forecast.Timestamp = pd.to_datetime(forecast['month'], format='%Y-%m')
        forecast.index = forecast.Timestamp
        forecast = forecast.resample('M').mean()

        df = df.append(forecast)
        # df.plot()

        # pred.predicted_mean.plot(ax=ax)
        # plt.show(block=True)

        return df
