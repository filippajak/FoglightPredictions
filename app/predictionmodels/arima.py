from statsmodels.tsa.api import ARIMA

class Arima:

    def predict(self, train, test, order, disp):
        history = [x for x in train.values]
        predictions = test.copy()
        for t in range(len(predictions.values)):
            model = ARIMA(history, order=order)
            model_fit = model.fit(disp=disp)
            output = model_fit.forecast(steps=1)
            yhat = output[0]

            predictions['marketshare'][t] = yhat[0]

            if t < len(test.values):
                obs = test.values[t]
                history.append(obs)
                print('predicted=%f, expected=%f' % (yhat, obs))
            else:
                print('predicted=%f' % yhat)
        return predictions

