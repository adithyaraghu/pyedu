import numpy as np
import pandas as pd

def isNaN(num):
    return num != num

my_data = np.linspace(20,50,12)
print(my_data)

my_data_labels = ['JAN','FEB', 'MAR', 'APR' , 'MAY' , 'JUN', 'JUL', 'AUG', 'SEP','OCT','NOV','DEC']
print(my_data_labels)

my_data_series = pd.Series(data=my_data,index=my_data_labels)
print(my_data_series)

my_data_series['ADI'] = 54.0

print("Modified array \n {mydata}".format(mydata= my_data_series))

other_data = np.linspace(30,90,12)
print(other_data)

other_data_labels = ['JAN','FEB', 'MAR', 'APR' , 'MAY' , 'JUN', 'JUL', 'AUG', 'SEP','OCT','NOV','DEC']
print(other_data_labels)
other_data_series = pd.Series(other_data,other_data_labels)
print(other_data_series)
other_data_series['ANANTH'] = 60.0

print("Modified array \n {OTHERdata}".format(OTHERdata= other_data_series))


new_data_series = my_data_series ** other_data_series

print("New data Series \n {}".format(new_data_series))

print(" Only NaNs :\n {}".format(new_data_series[isNaN(new_data_series)]))



