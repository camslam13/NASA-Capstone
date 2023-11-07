
import numpy as np
import tensorflow as tf
from keras.applications import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Define the image dimensions and number of classes
img_width, img_height = 150, 150
num_classes = 2

# Create a CNN model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Define data generators for training and testing
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'C:\Users\surfc\IdeaProjects\NASA-Capstone\train',
    target_size=(img_width, img_height),
    batch_size=32,
    class_mode='categorical')

test_generator = test_datagen.flow_from_directory(
    'C:\Users\surfc\IdeaProjects\NASA-Capstone\test',
    target_size=(img_width, img_height),
    batch_size=32,
    class_mode='categorical')

# Train the model
model.fit(train_generator, epochs=10, validation_data=test_generator)

# Evaluate the model
accuracy = model.evaluate(test_generator)[1]
print(f"Accuracy: {accuracy * 100:.2f}%")
