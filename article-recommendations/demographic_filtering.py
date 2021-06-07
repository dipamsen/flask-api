import numpy as np
import pandas as pd

df = pd.read_csv("articles.csv")
output = df.sort_values(by="total_events", ascending=False)[
    ["url", "title", "text", "lang", "total_events"]]
