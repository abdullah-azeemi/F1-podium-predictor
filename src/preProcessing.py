import pandas as pd

import pandas as pd

def processFeatures(df):
    for col in df.columns:
        if "bestLap" in col or "Top3Average" in col:
            df[col] = pd.to_timedelta(df[col], errors="coerce")
            df[col] = df[col].dt.total_seconds()

    df.fillna(df.mean(numeric_only=True), inplace=True)
    return df
