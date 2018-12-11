import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense,Flatten,Dropout,Activation
from keras.layers import Convolution2D,MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist
from keras import backend as K
K.set_image_dim_ordering('th')


data = pd.read_csv("train.csv")

print data.shape
pixel_data = data.iloc[:,1:]
label_data = data.iloc[:,0]

X_train = np.reshape(pixel_data,28,28)
print X_train.shape

print X_train[1,:]

"""
(X_train,y_train),(X_test,y_test) = mnist.load_data()
print X_train.shape

plt.imshow(X_train[0])

X_train = X_train.reshape(X_train.shape[0],1,28,28)
X_test = X_test.reshape(X_test.shape[0],1,28,28)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train/=255
X_test/=255

print y_train.shape

Y_train = np_utils.to_categorical(y_train,10)
Y_test = np_utils.to_categorical(y_test,10)

print Y_train[:10,:]

model = Sequential()

model.add(Convolution2D(32,3,3,activation = 'relu',input_shape = (1,28,28)))
model.add(Convolution2D(32,3,3,activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128,activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation = 'softmax'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X_train, Y_train, batch_size=32, nb_epoch=10, verbose=1)

score = model.evaluate(X_test,Y_test,verbose = 0)
"""
