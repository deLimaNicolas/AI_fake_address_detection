import pandas as pd

def get_data_frame(csv_path, delimiter):
  frame = pd.read_csv(csv_path, delimiter)
  return frame

