import pandas as pd

# get rows of DF where column named KEY has value VAL. 
# set kwarg AND to true/false for logical and/or filtering.
def filterDfByDict(df, fil, *, AND=True):
  ind = None
  for k,v in fil.items():
    if ind is None:
      ind = df[k] == v
      continue

    if AND:
      ind &= df[k] == v
    else:
      ind |= df[k] == v
    
  return df.loc[ind]

# Convert a row of a DF into dict. 
# set COLUMNS to a list of columns name to include (default all)
def createFilterByRow(df, columns=None):
  isSeries = isinstance(df, pd.Series)
  isDF = isinstance(df, pd.DataFrame)
  if not (isSeries or (isDF and df.shape[0] == 1)):
    raise Exception("Input df must only have one row.")

  # convert DF to Series
  if isDF:
    df = df.iloc[0]

  # default to all columns
  if columns is None:
    return df.to_dict()

  fil = {}
  for c in columns:
    if c not in df.index:
      raise Exception(f"Attempted to access non-existing column {c}")
    fil[c] = df[c]

  return fil
