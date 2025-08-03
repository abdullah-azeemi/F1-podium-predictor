import joblib
import pandas as pd
import os

## -- Configurations -- ###
dataPath = "../data/processed/2025_Hungary_ModelFeatures.csv"
modelPath = "../models/xgb_podium_predictor.pkl"

topK = 3 # podium positions

print("Loading model")
model = joblib.load(modelPath)

print("Loading race data")
features = pd.read_csv(dataPath)

drivers = features['Driver']

# Reordering features to match training columns
expected_columns = [
    'Sector3Time_mean',
    'Sector2Time_mean',
    'Sector1Time_mean',
    'AvgQualiPosition',
    'AvgRacePaceDelta',
    'Quali_Position',
    'Practice 3_Top3Average',
    'Practice 1_BestLap',
    'ThrottleAggressiveness',
    'avgBrake',
    'LowSpeedCornerPerf',
    'Practice 2_Top3Average'
]

features2025 = features[expected_columns] 
#print("\n Features used:", features2025.columns.tolist())

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