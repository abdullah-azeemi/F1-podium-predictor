import fastf1
import os

fastf1.Cache.enable_cache('../data/raw')

def loadSession(year, granPrix, sessionType):
  session = fastf1.get_session(year, granPrix, sessionType)
  session.load()
  return session

if __name__=="__main__":
  for session in ['FP1', 'FP2', 'FP3', 'Q', 'R']:
    s = loadSession(2024,'Hungary', session)
    print(f"{session} has been loaded: {s.event['EventName']} {s.event['EventDate']}")
    