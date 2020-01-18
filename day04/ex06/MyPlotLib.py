import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from FileLoader import FileLoader

class MyPlotLib:
    def histogram(self, data, features):
        for col in data.columns[1:]:
            if (data[col].dtype == 'int64'
                or data[col].dtype == 'float64'):
                plt.plot(data[col].values)
                plt.ylabel(col)
                plt.show()
        return

loader = FileLoader()
d = loader.load("../resources/athlete_events.csv")

mpl = MyPlotLib()
mpl.histogram(d, [""])