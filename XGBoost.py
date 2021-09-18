import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

dataset=pd.read_excel("city-of-bloomington-data/MLProject.xlsx")

ds=dataset.drop(["Primary Factor","Master Record Number","Collision Date", "Collision Time","Damage Estimate"],axis=1)
Y=dataset["Primary Factor"]

from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import LabelBinarizer
X1=ds['Township']
X2=ds['Roadway Junction Type']
X3=ds['Surface Condition']
X4=ds['Light Condition']

le= LabelEncoder()
Y=dataset["Primary Factor"]=le.fit_transform(dataset["Primary Factor"])
#y = LabelBinarizer().fit_transform(df.Countries)
X1New = le.fit_transform(X1)
X1New = X1New.reshape(-1,1)
X2New = le.fit_transform(X2)
X2New = X2New.reshape(-1,1)
X3New = le.fit_transform(X3)
X3New = X3New.reshape(-1,1)
X4New = le.fit_transform(X4)
X4New = X4New.reshape(-1,1)

v=np.asarray(ds['Vehicles Involved'])
v = v.reshape(-1,1)
concatinated=np.concatenate((X1New,X2New,X3New,X4New,v),axis=1)
ds= pd.DataFrame(concatinated)

traindata,testdata,trainlabel,testlabel=train_test_split(ds,Y,test_size=0.33,random_state=0)

import xgboost as xgb
import time
debut=time.time()
model = xgb.XGBRegressor(max_depth=25,learning_rate=0.5)
model.fit(traindata,trainlabel)
temps=time.time()-debut
pred=model.predict(testdata)
pred=pred.reshape(-1,1)

from sklearn.metrics import mean_squared_error
import math

mse = mean_squared_error(testlabel,pred)

print('RMSE',math.sqrt(mse))

from sklearn.metrics import r2_score
r=r2_score(testlabel,pred)
print(r)
from sklearn.metrics import explained_variance_score
EV=explained_variance_score(testlabel,pred)
print("Explained variance: %f" %(EV))
