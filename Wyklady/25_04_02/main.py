import numpy as np
import pandas as pd


dane = pd.Series([10,20,30,40,5000,60,70,90,100])

srednia = dane.mean()

print(f"srednia: {srednia}")