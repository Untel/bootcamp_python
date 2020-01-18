from FileLoader import FileLoader

def youngestFellah(data, year):
    els = data.loc[data['Year'] == year]
    return {
        'M': (els.loc[els['Sex'] == 'M'])['Age'].min(),
        'F': (els.loc[els['Sex'] == 'F'])['Age'].min(),
    }

loader = FileLoader()
d = loader.load("../resources/athlete_events.csv")
print(youngestFellah(d, 2004))