import joblib 
import pandas as pd
import os

## -- Configurations -- ###
modelPath = "../models/xgb_podium_predictor.pkl"
dataPath = "../data/processed/2025gp_features.csv"
topK = 3 # podium positions

print("Loading model")
model = joblib.load(modelPath)

print("Load Information")
df2025 = pd.read_csv(dataPath)

featureCols = model.feature_names_in
x2025 = df2025[featureCols]

print("The Predicted Positions are \n")
df2025['PredictedFinish'] = model.predict(x2025)

dfSorted = df2025.sort_values('PredictedFinish').reset_index(drop=True)

#printing who will be at the podium
print(dfSorted[['Driver', 'PredictedFinish']].head(topK))

