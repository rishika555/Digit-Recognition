import pandas as pd #pip install pandas
from sklearn.utils import shuffle #pip install scikit-learn

 
data = pd.read_csv('dataset.csv')
data = shuffle(data)
print(data)

X = data.drop(["label"],axis=1)
Y= data["label"]

import matplotlib.pyplot as plt
import cv2
idx = 314
img = X.loc[idx].values.reshape(28,28)
print(Y[idx])
plt.imshow(img)

from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y = train_test_split(X,Y, test_size = 0.2)


