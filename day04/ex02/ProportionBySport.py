from FileLoader import FileLoader

def proportionBySport(dataframe, year, sport, gender):
    els = dataframe.loc[(dataframe['Year'] == year) & (dataframe['Sex'] == 'F')]
    ath = els['ID'].nunique()
    fem = els.loc[els['Sport'] == sport]['ID'].nunique()
    return fem / ath

# loader = FileLoader()
# d = loader.load("../resources/athlete_events.csv")
# print(proportionBySport(d, 2004, 'Tennis', 'F'))