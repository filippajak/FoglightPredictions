from app.model.historical_datapath import HistoricalDatapath


class DataframeConverter:

    def get_future_datapaths(self, df, country):
        paths = list()
        df_dict = df.to_dict()
        print(df_dict)
        for item, datapaths in df_dict.items():
            i = HistoricalDatapath(datapaths, item, country)
            paths.append(i)

        return paths





