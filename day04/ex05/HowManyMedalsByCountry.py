from FileLoader import FileLoader

def howManyMedalsByCountry(data, name):
    els = data.loc[data['Team'] == name]
    grp = els.groupby(['Year'])
    ret = {}
    for year, row in grp:
        ret[year] = {
            'G': row.loc[row['Medal'] == 'Gold']['Event'].nunique(),
            'S': row.loc[row['Medal'] == 'Silver']['Event'].nunique(),
            'B': row.loc[row['Medal'] == 'Bronze']['Event'].nunique(),
        }
    return ret

loader = FileLoader()
d = loader.load("../resources/athlete_events.csv")

print(howManyMedalsByCountry(d, 'France'))