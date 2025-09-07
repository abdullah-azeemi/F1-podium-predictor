import joblib
import pandas as pd
import os

## -- Configurations -- ###
script_dir = os.path.dirname(os.path.abspath(__file__))
dataPath = os.path.join(script_dir, "..", "data", "processed", "2025_Monza_ModelFeatures.csv")
modelPath = os.path.join(script_dir,"..", "models", "xgb_monza_podium_predictor.pkl")

# Validate paths 
if not os.path.exists(modelPath):
	raise FileNotFoundError(f"Model file not found at: {modelPath}")
if not os.path.exists(dataPath):
	raise FileNotFoundError(f"Data file not found at: {dataPath}")

topK = 3 

print("Loading model")
model = joblib.load(modelPath)

print("Loading race data")
features = pd.read_csv(dataPath)

drivers = features['Driver']

expected_columns = [
    'Quali_Position',
  'AvgQualiPosition',
  'AvgRacePaceDelta',
  'Practice 1_BestLap',
  'Practice 3_Top3Average'
]

features2025 = features[expected_columns] 

predictedPositions = model.predict(features2025)

results = pd.DataFrame({
    'Driver': drivers,
    'PredictedPosition': predictedPositions
})

results = results.sort_values(by='PredictedPosition').reset_index(drop=True)

# ANSI escape codes for colors
# \033[93m = Yellow
# \033[97m = White
# \033[90m = Black
# \033[0m = Reset all formatting
# \033[1m = Bold
YELLOW = "\033[93m"
WHITE = "\033[97m"
GRAY = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Unicode icons for medals
# 🥇 = Gold Medal
# 🥈 = Silver Medal
# 🥉 = Bronze Medal
medals = ["🥇", "🥈", "🥉"]

print("\n" + BOLD + "Predicted Podium for 2025 Hungarian GP:" + RESET)
for idx, row in results[['Driver']].head(topK).iterrows():
    if idx == 0:
        # Gold medal
        color = YELLOW
    elif idx == 1:
        # Silver medal
        color = WHITE
    else:
        # Bronze medal
        color = GRAY
    
    # Print the line with the icon, color, and driver name
    print(f"{BOLD}{color}{medals[idx]}{RESET} {row['Driver']}")