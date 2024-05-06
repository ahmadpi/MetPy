import pandas as pd
from metpy.io.gempak import GempakGrid, GempakSounding, GempakSurface

res = pd.read_csv('wmkk_2023062700.txt')

print(res)