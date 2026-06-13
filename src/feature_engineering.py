def create_time_features(df, time_col):
    df[time_col] = pd.to_datetime(df[time_col])
    df['hour'] = df[time_col].dt.hour
    df['day'] = df[time_col].dt.dayofweek
    return df