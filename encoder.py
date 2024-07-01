def encode_data(dataframe_series):
  if dataframe_series.dtype=='object':
    dataframe_series = LabelEncoder().fit_transform(dataframe_series)
    return dataframe_series