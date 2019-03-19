# library
import matplotlib.pyplot as plt


class StackedAreaPlotter:

    def draw(self, dataframe, country):

        # plot

        # df1 = dataframe[:"2019-01"]
        # df2 = dataframe["2019-01":]

        dataframe.plot.area(title=country)
        # df2.plot.area(title=country, ax=ax)

        plt.show(block=True)
