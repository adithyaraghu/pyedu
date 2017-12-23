import pandas as pd
import numpy as np
import matplotlib as mp
import seaborn as sns

class PlotMe :
    static_equivalent = 34.32

    def __init__(self):
        self.name = "default"
        self.age = 0
        self.species = "human"

plot = PlotMe()
print(plot.name,":",plot.age,",",plot.species,",",plot.static_equivalent,PlotMe.static_equivalent )
