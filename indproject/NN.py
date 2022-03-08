import eel
import numpy as np
from tensorflow import keras
from keras.layers import Dense, Flatten
from keras.datasets import mnist
from PIL import Image
import matplotlib.pyplot as plt
from keras.models import load_model

eel.init('web')


@eel.expose
def go(data):
    def formating(pixels):
        pixels = np.array(pixels)
        pixels.shape = (392, 392)
        pixels = Image.fromarray(pixels)
        pixels = pixels.resize((28, 28), Image.ANTIALIAS)
        return pixels

    img = formating(data)
    img = np.expand_dims(img, axis=0)
    img = img / 255
    answer = neuralNet.predict(img)
    x= answer
    x = list(map(lambda x: round(x * 100, 2), x[0]))
    print(x)
    eel.write(x)


@eel.expose
def learning(epochs):
    epochs = int(epochs)
    (train_images, train_answer), (test_images, test_answer) = mnist.load_data()
    train_images = train_images / 255
    test_images = test_images / 255
    train_answer = keras.utils.to_categorical(train_answer, 10)
    test_answer = keras.utils.to_categorical(test_answer, 10)
    his = neuralNet.fit(train_images, train_answer, batch_size=100,
                  epochs=epochs, validation_split=0.2)
    neuralNet.evaluate(test_images, test_answer)
    neuralNet.save('save.h5')
    plt.show()


@eel.expose
def make_defoultnn(neirons):
    neirons = int(neirons)
    global neuralNet
    neuralNet = keras.Sequential([
        Flatten(input_shape=(28, 28, 1)),
        Dense(neirons, activation='relu'),
        Dense(10, activation='softmax')])
    neuralNet.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])


neuralNet = load_model('save.h5')
eel.start('main.html', size=(830, 550), mode='chrome', port=8080, host='localhost')
