import os
import sklearn
from sklearn import ensemble
import pandas
import numpy
import scipy
import matplotlib

def isnan(num):
    return num != num

def transfo(rm):
    for col in rm.columns :
        if( isinstance(col,str) and ' ' in col ):
            print("combo column : {}".format(col))
            newlist = col.split(' ')
            for colname in newlist:
                if colname not in rm.columns:
                    print(" NEW colname {}".format(colname))
                    rm[colname] = rm[col]
                else:
                    print("Existing colname {}".format(colname))
                    rm[colname] = rm[colname].astype(str) + rm[col].astype(str)
            if col in rm.columns:
                del rm[col]


train_path = os.path.join("/home/adithyaraghuraman/Downloads","titanic_train.csv")
data_others = pandas.read_csv(train_path,header=0,dtype={'PassengerId':numpy.int32,
                                                              'Survived':str,
                                                              'Sex':str,
                                                              'Age':numpy.float64,
                                                              'SibSp':numpy.int32,
                                                              'Parch':numpy.int32,
                                                              'Ticket':str,
                                                              'Fare':numpy.float64,
                                                              'Cabin':str,
                                                              'Embarked':str},
                       usecols=['PassengerId','Sex','Age','SibSp','Parch','Fare','Embarked'])
demo_other_y = pandas.DataFrame( pandas.read_csv(train_path,header=0,dtype={'PassengerId':numpy.int32,
                                                              'Survived':str,
                                                              'Sex':str,
                                                              'Age':numpy.float64,
                                                              'SibSp':numpy.int32,
                                                              'Parch':numpy.int32,
                                                              'Ticket':str,
                                                              'Fare':numpy.float64,
                                                              'Cabin':str,
                                                              'Embarked':str},
                       usecols=['Survived']))

data_cabin = pandas.read_csv(train_path,header=0,dtype={'PassengerId':numpy.int32,
                                                              'Survived':str,
                                                              'Sex':str,
                                                              'Age':numpy.float64,
                                                              'SibSp':numpy.int32,
                                                              'Parch':numpy.int32,
                                                              'Ticket':str,
                                                              'Fare':numpy.float64,
                                                              'Cabin':str,
                                                              'Embarked':str},
                       usecols=['PassengerId','Cabin'])


demo_other = pandas.DataFrame(data_others)
demo_other['Age'].fillna(value=0.00,inplace=True)
demo_other['Fare'].fillna(value=0.00,inplace=True)
demo_cabin = pandas.DataFrame(data_cabin)
# print("demo_other is \n{}\n".format(demo_other.head()))

columnsToEncode = ['Sex','Embarked']
demo_cabin['Cabin'] = demo_cabin['Cabin'].fillna(value='N/A')
for cabin_val in demo_cabin['Cabin'].unique():
    if (isinstance(cabin_val, str) and ' ' in cabin_val):
        # print("combo column : {}".format(cabin_val))
        newlist = cabin_val.split(' ')
        for colname in newlist:
            if not colname in demo_other.columns:
                # columnsToEncode.append("Cabin_"+colname)
                demo_other["Cabin_"+colname] = 0
    else:
        if not cabin_val in demo_other.columns:
            # columnsToEncode.append("Cabin_"+ cabin_val)
            demo_other["Cabin_"+cabin_val] = 0

for index,row in demo_other.iterrows():
    # print("index={},PassengerId={}".format(index,row['PassengerId']))
    cabin_vals = demo_cabin[demo_cabin['PassengerId']==row['PassengerId']]['Cabin'].values[0]
    if(isinstance(cabin_vals, str) and ' ' in cabin_vals):
        newlist = cabin_vals.split(' ')
        for cabin in newlist:
            demo_other.set_value(index,"Cabin_"+cabin,1)
    else:
        demo_other.set_value(index,"Cabin_"+cabin_vals,1)

# print(demo_other.head())

print("\ncolumnsToEncode: {}\n".format(columnsToEncode))
data_dummies = pandas.get_dummies(demo_other, columns=columnsToEncode)
# print("\nFeatures after get_dummies:{}\n".format(list(data_dummies.columns)))
print(data_dummies.head())

gbrt = ensemble.gradient_boosting.GradientBoostingClassifier(random_state=0, learning_rate=0.01)
gbrt.fit(data_dummies, demo_other_y)


# print(demo_cabin[demo_cabin['PassengerId']==840]['Cabin'].values[0])
#
# print(s)
# print(demo_other.head())
# for row in demo_other.itertuples():
#     print(row)

# demo_cabin = demo_cabin.pivot(index='PassengerId',columns='Cabin', values='PassengerId')
# demo_cabin[isnan(demo_cabin)] = "N/A"

# print(demo_cabin.head())
# transfo(demo_cabin)
# print(demo_cabin)

# print("demo_cabin is \n{}\n".format(demo_cabin.head()))
# cabin_values_array = demo_cabin['Cabin'].ravel()
# print(cabin_values_array)


# a = pandas.merge(left=demo_other, right=demo_cabin, left_on='PassengerId', right_on='PassengerId')
# print("a is \n{}\n".format(a.head()))
# print("get dummies is \n{}\n".format(pandas.get_dummies(demo_df,columns=['Survived','Sex','Embarked'])))
