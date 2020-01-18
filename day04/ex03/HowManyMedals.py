from FileLoader import FileLoader

def howManyMedals(df, name):
    ath = df.loc[df['Name'] == name]
    ret = {}
    for year, row in ath.groupby(['Year']):
        ret[year] = {
            'G': len(row.loc[row['Medal'] == 'Gold']),
            'S': len(row.loc[row['Medal'] == 'Silver']),
            'B': len(row.loc[row['Medal'] == 'Bronze'])
        }
    return ret

loader = FileLoader()
d = loader.load("../resources/athlete_events.csv")
print(howManyMedals(d, 'Kjetil Andr Aamodt'))
