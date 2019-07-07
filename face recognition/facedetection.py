'''
Steps for face detection:
1. Convolution
2. Max Pooling
3. Flattening
4. Full Connection

convolution:
Input image in the form of matrix x feature detector= feature Map

Max pooling:
Feature map ---- Max pooling ----> pooled map

Flattening:
Pooled map ---- Flattening ----> Array

Full Connection:
Complete neural network implementation.

Summary:

Input Image ---Convolution---> Convolution Layer --- Pooling ---> Pooling Layer
'''

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
import cv2
import numpy as np

# Step 1 Initializing  the CNN
classifier = Sequential()

#  Step 1
classifier.add(Convolution2D(32, 3, 3, input_shape=(64, 64, 3), activation='relu'))
# 32-features detector into 3*3 matrix
# reshape transform all images into single format
# and 3 is for color image

#  Step 2 Pooling

classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Step 3 Flattening
classifier.add(Flatten())

# Step 4 Full Connection
classifier.add(Dense(output_dim=128, activation='relu'))
classifier.add(Dense(output_dim=1, activation='sigmoid'))
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("All Step Done")

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    'data/train',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    'data/test',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

classifier.fit_generator(
    train_generator,
    steps_per_epoch=8000,
    epochs=1,
    validation_data=validation_generator,
    validation_steps=2000)
classifier.save("model.h5")
print("Model Saved")

print("After all step")
img = cv2.imread('test.jpg')
img = cv2.resize(img, (32, 32))
img = np.reshape(img, [1, 32, 32, 3])
classes = classifier.predict_classes(img)

print(classes)
