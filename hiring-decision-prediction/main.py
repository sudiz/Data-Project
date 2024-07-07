import csv
import numpy as np
import pandas as pd
import sklearn

print(1)


import os
for dirpath, dirname, filenames in os.walk('D:\出国\work-prepare\hiring-decision-prediction'):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
