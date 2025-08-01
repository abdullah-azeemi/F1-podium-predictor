import fastf1
from fastf1 import plotting
import pandas as pd
import numpy as np

def getDriverTelemetry(granPrix:str, year:int, sessionType:str, driver:str):
    session = fastf1.get_session(year, granPrix, sessionType)
    session.load()
    
    laps = session.laps.pick_driver(driver).pick_fastest()
    if laps.empty:
      return None
    
    telemetry = laps.get_car_data().add_distance()
    return telemetry
  
  
def extractCarFeatures(telemetry: pd.DataFrame) -> dict:
  if telemetry is None or telemetry.empty:
    return {
      'maxSpeed': np.nan,
      'avgCornerSpeed': np.nan,
      'avgThrottle': np.nan,
      'avgBrake': np.nan,
    }
    
  maxSpeed = telemetry['Speed'].max()
  cornerSpeed = telemetry[telemetry['Speed'] < 160]['Speed'].mean()
  avgThrottle = telemetry['Throttle'].mean()
  avgBrake = telemetry['Brake'].mean()
  
  return { 
    'maxSpeed': maxSpeed,
    'avgCornerSpeed': cornerSpeed,
    'avgThrottle': avgThrottle,
    'avgBrake': avgBrake
  }
  
  
def generateFeatures(grandPrix: str, year: int, sessionName='Q') -> pd.DataFrame:
    session = fastf1.get_session(year, grandPrix, sessionName)
    session.load()
    drivers = session.drivers
    feature_list = []

    for drv in drivers:
        drv_code = session.get_driver(drv)['Abbreviation']
        telemetry = getDriverTelemetry(grandPrix, year, sessionName, drv_code)
        dynamics = extractCarFeatures(telemetry)
        dynamics['Driver'] = drv_code
        feature_list.append(dynamics)

    return pd.DataFrame(feature_list)