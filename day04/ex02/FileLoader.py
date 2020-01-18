import pandas as pd

class FileLoader:
    def load(self, path):
        els = pd.read_csv(path)
        w, h = els.shape
        print("Loading dataset of %dx%d" % (w, h))
        return els

    def display(self, data, n):
        print((data.head if n >= 0 else data.tail)(n if n >= 0 else -n))

# loader = FileLoader()
# d = loader.load("../resources/athlete_events.csv")
# loader.display(d, 0)