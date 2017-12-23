import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0,11,11)
y = x**2


figure = plt.figure()
#axes1 = figure.add_axes([0,0,  1,1])
axes1 = figure.add_axes([0.1,0.1,0.8,0.8])
axes1.set_xlabel("Main X")
axes1.set_ylabel("Main Y")

axes2 = figure.add_axes([0.2,0.5,0.4,0.3 ])
axes2.set_xlabel("sub X")
axes2.set_ylabel("sub Y")
plt.show()
