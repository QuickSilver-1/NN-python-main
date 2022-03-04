#this is dont work now

from statistics import mode
import eel
import numpy as np
from tensorflow import keras
from keras.layers import Dense, Flatten
from keras.datasets import mnist
from PIL import Image

eel.init('Web')


def format(pixels):
    print(11111)
    print(pixels)
    pixels = np.array(pixels)
    pixels.shape = (392, 392)
    img = Image.fromarray(pixels, mode='L')
    img = img.resize((28, 28))
    return img


def learning(model):
    (train_images, train_answer), (test_images, test_answer) = mnist.load_data()
    train_images = train_images / 255
    test_images = test_images / 255
    train_answer = keras.utils.to_categorical(train_answer, 10)
    test_answer = keras.utils.to_categorical(test_answer, 10)

    model.fit(train_images, train_answer, batch_size=40,
              epochs=1, validation_split=0.2)
    model.evaluate(test_images, test_answer)


@eel.expose
def go():
    img = format(eel.gray_format())
    img = np.expand_dims(img, axis=0)
    answer = neuralNet.predict(img)
    x = np.argmax(answer)
    return x


neuralNet = keras.Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(100, activation='relu'),
    Dense(10, activation='softmax')
])
neuralNet.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

eel.start('main.html', size=(830, 600), mode='chrome', port=8081)

