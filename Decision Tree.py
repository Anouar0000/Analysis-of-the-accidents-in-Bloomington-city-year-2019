import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

dataset=pd.read_excel("city-of-bloomington-data/MLProject.xlsx")

label=dataset["Primary Factor"]
ds=dataset.drop(["Primary Factor","Master Record Number","Collision Date", "Collision Time","Damage Estimate"],axis=1)

from sklearn.preprocessing import LabelEncoder 
X1=ds['Township']
X2=ds['Roadway Junction Type']
X3=ds['Surface Condition']
X4=ds['Light Condition']
le= LabelEncoder()
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
traindata,testdata,trainlabel,testlabel=train_test_split(ds,label,test_size=0.33,random_state=0)

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion="gini", random_state= 0,max_depth=6,min_samples_split=12,min_samples_leaf=4)
model.fit(traindata,trainlabel)
pred=model.predict(testdata)
#calcul de l'accuracy
ACC=accuracy_score(testlabel, pred)*100
print(ACC)

print(classification_report(testlabel,pred))
#CREATION DE CONFUTION MATRIX
CM =confusion_matrix(testlabel,pred)
print("this the confusion mat: ",CM)