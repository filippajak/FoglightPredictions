import matplotlib.pyplot as plt

class DeviceMarketsharePlotter():

  def draw_plot_for_all_devices(self, paths):

    for datapath in paths:

      raw_x = list(dict(sorted(datapath.historical_marketshares.items())).keys())
      raw_y = list(dict(sorted(datapath.historical_marketshares.items())).values())

      x, y = zip(*sorted(zip(raw_x, raw_y)))

      label = str(datapath.handset + ' ' + datapath.country)

      plt.plot(x, y, label=label)
      plt.legend()

    plt.show(block=True)


    

