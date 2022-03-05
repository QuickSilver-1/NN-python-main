import eel
import numpy as np
from tensorflow import keras
from keras.layers import Dense, Flatten
from keras.datasets import mnist
from PIL import Image
import matplotlib.pyplot as plt

eel.init('D:/prog/indproject/Web')


@eel.expose
def go(data):
    def formating(pixels):
        pixels = np.array(pixels)
        pixels.shape = (392, 392)
        pixels = Image.fromarray(pixels)
        pixels = pixels.resize((28, 28), Image.ANTIALIAS)
        pixels = np.array(pixels)
        return pixels

    img = formating(data)
    img = np.expand_dims(img, axis=0)
    img = img / 255
    answer = neuralNet.predict(img)
    x, y = answer, np.argmax(answer)
    eel.write(x, y)
    print(x)
    print(y)

@eel.expose
def learning():
    (train_images, train_answer), (test_images, test_answer) = mnist.load_data()
    train_images = train_images / 255
    test_images = test_images / 255
    train_answer = keras.utils.to_categorical(train_answer, 10)
    test_answer = keras.utils.to_categorical(test_answer, 10)
    neuralNet.fit(train_images, train_answer, batch_size=40,
              epochs=5, validation_split=0.2)
    neuralNet.evaluate(test_images, test_answer)


neuralNet = keras.Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(100, activation='relu'),
    Dense(10, activation='softmax')
])
print(neuralNet.summary())
neuralNet.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

eel.start('main.html', size=(830, 550), mode='chrome', port=0)









