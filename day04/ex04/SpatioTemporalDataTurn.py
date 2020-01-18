from FileLoader import FileLoader

class SpatioTemporalData():
    def __init__(self, data):
        self.d = data

    def where(self, date):
        place = self.d.loc[self.d['Year'] == date]['City'].head(1).values
        return place

    def when(self, place):
        date = self.d.loc[self.d['City'] == place]
        els = date['Year'].unique()
        return list(els)

loader = FileLoader()
d = loader.load("../resources/athlete_events.csv")
std = SpatioTemporalData(d)

print(std.where(1896))
print(std.when('Paris'))