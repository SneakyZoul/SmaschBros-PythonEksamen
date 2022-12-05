import os

import numpy
import tensorflow as tf
from tensorflow import keras
from keras.constraints import maxnorm
from keras.utils import np_utils
from keras.datasets import cifar10
from keras import Sequential
import matplotlib.pyplot as plt
from keras.utils import to_categorical # to get a one-hot incoding of the target data
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

from config.definitions import ROOT_DIR
from data import resizedImages
import imageDataframe as im


(x_train, y_train), (x_test, y_test) = im.get_images(os.path.join(ROOT_DIR, 'data', 'resizedImages'))
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
#her finder vi ud af at den er 32X32
image_index = 0
print(y_train[image_index])
plt.imshow(x_train[image_index], cmap='Greys')
plt.show()



(x_train, y_train),(x_test, y_test)=(x_train_original, y_train_original),(x_test_original, y_test_original) =cifar10.load_data()
image_size = (32*32)*3
x_train = x_train.reshape(x_train.shape[0],image_size) # x_train = (60000,784)
print(x_train)
x_train = x_train.astype('float32')
x_train /= 255

x_test = x_test.reshape(x_test.shape[0],image_size)
x_test = x_test.astype('float32')
x_test /= 255

x_train[35]
#I denne del, oneHot encode vi, så systemtet kan finde ud af det.
num_classes =10

y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)
y_test[:4]

# test out the to_categorical method
print(to_categorical([0],10))
print(to_categorical([1],10))
print(to_categorical([2],10))

model = Sequential()
# define each layer in the network
 # the simplest layer type

input_layer = Dense(units=500,  # 512 units (nodes) is an arbitrary number (might be ajusted later up or down to see what gives most accuracy)
                activation='sigmoid', # activation is the activation function used to pass dot product of all inputs and weights through
                input_shape=(image_size,)) #32x32 for the mnist image size (must be an iterable, therefore the comma)
print(image_size)
# add hidden layer
model.add(input_layer)
# add another  hidden layer
model.add(Dense(units=500,activation='sigmoid'))


# add an output layer
model.add(Dense(units=10,
                activation='softmax',)) # softmax nonlinearity function for mapping the neural network activation to the categories               ))
model.summary()


# Now train the model
model.compile(loss='categorical_crossentropy', # loss is how to meassure how wrong the model is on its predictions
             optimizer='sgd', # "stochastic gradient descent" is a way to tell algorithm how to improve
             metrics=['accuracy'], # what do we care about in our model
             )
model.fit(x_train,
         y_train,
         epochs=5,
         verbose=True,
         validation_split=0.1) # checking periodically how well we are doing


_, (ax1, ax2, ax3) = plt.subplots(1,3)
ax1.imshow(x_test_original[0],cmap='Greys')
ax2.imshow(x_test_original[1],cmap='Greys')
ax3.imshow(x_test_original[2],cmap='Greys')


results = model.evaluate(x_test, y_test)
print(f'test loss, test acc:', results)

# Generate predictions (probabilities -- the output of the last layer)
# on new data using `predict`
print('\n# Generate predictions for 3 samples')
###predictions = model.predict(x_test[:7])
predict_x = model.predict(x_test[:3])
#print('predictions shape:', predictions.shape)
#print(predictions)
###print('predict classes',model.predict_classes(x_test[:7]))
class_x=np.argmax(predict_x,axis=1)
print('predict classes',class_x)
