import numpy as np
import pandas as pd

def isNotNaN(num):
    return not (num != num)

def isNaN(num):
    return num != num

def ws(w):
    print('w {},{},{}'.format(w,type(w), (isinstance(w,str) and ' ' in w )))
    if isinstance(w,str) and (' ' in w):
        True
    else:
        False
titanic_data  = pd.read_csv('/home/adithyaraghuraman/Downloads/titanic_train.csv')
print("****************** START : Titanic Data *********************** \n{}\n****************** END : Titanic Data ***********************\n".format(titanic_data))
print("\n****************** START : Titanic Data With Cabin C123 *********************** \n{}\n****************** END : Titanic Data With Cabin C123 ***********************".format( titanic_data[(isNaN(titanic_data['Cabin']))]))
titanic_data['Cabin'].fillna(0, inplace=True)
print("titanic_data....... : {}\n END-----\n".format(titanic_data))
records = titanic_data.pivot(index='PassengerId' ,columns="Cabin", values='PassengerId')
print("Records....... : {}\n END-----\n".format(records))
records[isNaN(records)] = 0
print(records.columns.astype(str))


columns =  [col for col in records.columns if( isinstance(col,str) and ' ' in col )  ]

for col in records.columns :
    if( isinstance(col,str) and ' ' in col ):
        print("combo column : {}".format(col))
        newlist = col.split(' ')
        for colname in newlist:
            if colname not in records.columns:
                print(" NEW colname {}".format(colname))
                records[colname] = records[col]
            else:
                print("Existing colname {}".format(colname))
                records[colname] = records[colname] + records[col]
        if col in records.columns:
            del records[col]


print("records final \n {} ".format(records))

print("Final Output \n{}".format(titanic_data.merge(records,left_index=True,right_index=True)));

