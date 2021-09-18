import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

Dataset = pd.read_excel("city-of-bloomington-data/MLProject.xlsx")


Date=Dataset["Collision Date"]
Damage=Dataset["Damage Estimate"]

L=[]
cnt=[]
k=""

for i in Date:
    if i ==k:
        pass

    else:
        L.append(i)
        cnt.append(list(Date).count(i))
    k=i

print(len(L))
print(cnt)

D=[]
s=Damage[0]
for i in range(1,len(Damage)):
    if Date[i]==Date[i-1]:
        s+=Damage[i]
    else:
        D.append(s)
        s=Damage[i]
D.append(s)
print(D)

L=np.array(L)
cnt=np.array(cnt)
D=np.array(D)
test=L

le= LabelEncoder()
L = le.fit_transform(L)

L = L.reshape(-1,1)
cnt = cnt.reshape(-1,1)
D = D.reshape(-1,1)


DataNew=np.concatenate((L,cnt,D),axis=1)

DataNew=pd.DataFrame(DataNew,columns=["Date","Nb_Accidents","Damages estimated"])

plt.plot(test,DataNew["Nb_Accidents"])
plt.title('Distribution des données.')
plt.show()

from sklearn.linear_model import LinearRegression


X=DataNew["Date"]
Y=DataNew["Nb_Accidents"]
X=np.array(X)
Y=np.array(Y)

X=X.reshape(-1,1)
Y=Y.reshape(-1,1)

model=LinearRegression()
model.fit(X,Y)

#3
a=model.coef_ #la valeur de a
print("this is the a : ",a)
#b
b=model.intercept_ #la valeur de b
print("this is the b : ",b )


pred=model.predict(X)

from sklearn.metrics import r2_score
r=r2_score(Y,pred)
print("r: ",r)

#5

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(Y,pred)
import math
print('RMSE',math.sqrt(mse))

from sklearn.metrics import explained_variance_score
EV=explained_variance_score(Y, pred)
print("Explained variance: %f" % (EV))

print('prediction for test step', model.predict([[364]]))

