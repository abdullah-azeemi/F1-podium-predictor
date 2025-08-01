import fastf1
import pandas as pd
from fastf1 import plotting

plotting.setup_mpl()

def getBestLaps(session):
  laps = session.laps.pick_quicklaps()
  bestLaps = laps.groupby('Driver')['LapTime'].min().reset_index()
  bestLaps.columns = ['Driver', f'{session.name}_BestLap']
  return bestLaps

def getAvg_top3Laps(session):
  laps = session.laps.pick_quicklaps()
  averageLaps = []
  for driver in laps['Driver'].unique():
    driverLaps = laps[laps['Driver'] == driver].nsmallest(3, 'LapTime')
    average = driverLaps['LapTime'].mean()
    averageLaps.append({'Driver' : driver, f'{session.name}_Top3Average': average})
  
  return pd.DataFrame(averageLaps)

def getQualiResults(session):
  df = session.results[['Abbreviation', 'Position']].copy()
  df.columns = ['Driver', 'Quali_Position']
  
  return df

def getRacePositions(session):
  df = session.results[['Abbreviation', 'ClassifiedPosition']].copy()
  df.columns = ['Driver', 'Race_result']
  
  return df