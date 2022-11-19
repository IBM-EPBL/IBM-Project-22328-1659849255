import pandas as pd 
import numpy as np 
from sklearn.linear_model import LogisticRegression 
data = pd.read_csv('./Heart.csv')
variety_mappings = {0: 'Absence', 1: 'Presence'}

# Encoding the target variables to integers
data = data.replace(['Absence', 'Presence' ], [0, 1])

X = data.iloc[:, 0:-1] 
y = data.iloc[:, -1]

logreg = LogisticRegression(max_iter=1000) 
logreg.fit(X, y)

def classify(a, b, c, d,e,f,g,h,i,j,k,l,m):
    arr = np.array([a, b, c, d,e,f,g,h,i,j,k,l,m]) # Convert to numpy array
    arr = arr.astype(np.float64) # Change the data type to float
    query = arr.reshape(1, -1) # Reshape the array
    prediction = variety_mappings[logreg.predict(query)[0]] # Retrieve from dictionary
    return prediction 