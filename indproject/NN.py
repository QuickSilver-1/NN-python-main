import eel
import numpy as np
from tensorflow import keras
# from keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D
# from keras.datasets import mnist
from keras.models import load_model
from PIL import Image


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
    x = answer
    x = list(map(lambda x: round(x * 100, 2), x[0]))
    eel.write(x)


# def learning(epochs):
#     epochs = int(epochs)
#     (train_images, train_answer), (test_images, test_answer) = mnist.load_data()
#     train_images = train_images / 255
#     test_images = test_images / 255
#     if code == 1:
#         train_images = np.expand_dims(train_images, axis=3)
#         test_images = np.expand_dims(test_images, axis=3)
#     train_answer = keras.utils.to_categorical(train_answer, 10)
#     test_answer = keras.utils.to_categorical(test_answer, 10)
#     neuralNet.fit(train_images, train_answer, batch_size=128,
#                   epochs=epochs, validation_split=0.2)
#     neuralNet.evaluate(test_images, test_answer)
#     if code == 1:
#         neuralNet.save('better.h5')
#     else:
#         neuralNet.save('defoult.h5')
#     score = neuralNet.evaluate(test_images, test_answer, verbose=0)
#     print('Потери на тесте:', score[0])
#     print('Точность на тесте:', score[1])

# def make_defoultnn(neirons):
#     neirons = int(neirons)
#     global neuralNet
#     global code
#     code = 0
#     neuralNet = keras.Sequential([
#         Flatten(input_shape=(28, 28, 1)),
#         Dense(neirons, activation='relu'),
#         Dense(10, activation='softmax')])
#     neuralNet.compile(optimizer='adam',
#                       loss='categorical_crossentropy',
#                       metrics=['accuracy'])
#     neuralNet.save('defoult')


# def make_betternn():
#     global neuralNet
#     global code
#     code = 1
#     neuralNet = keras.Sequential([
#         Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(28,28,1)),
#         MaxPooling2D((2, 2), strides=2),
#         Conv2D(64, (3, 3), padding='same', activation='relu'),
#         MaxPooling2D((2, 2), strides=2),
#         Dropout(0.25),
#         Flatten(),
#         Dense(256, activation='relu'),
#         Dropout(0.5),
#         Dense(10, activation='softmax')
#     ])
#     neuralNet.compile(optimizer='adam',
#                       loss='categorical_crossentropy',
#                       metrics=['accuracy'])
#     neuralNet.save('better')


@eel.expose
def load_model_nn(model):
    global neuralNet
    if model == 'perceptron':
        neuralNet = load_model('defoult.h5')
    else:
        neuralNet = load_model('better.h5')
    test = np.array([[0]*28]*28)
    test = np.expand_dims(test, axis=0)
    neuralNet.predict(test)


# make_defoultnn(256)
# learning(30)
# make_betternn()
# learning(30)


neuralNet = load_model('defoult.h5')
test = np.array([[0]*28]*28)
test = np.expand_dims(test, axis=0)
neuralNet.predict(test)
eel.start('main.html', size=(950, 700),
          mode='chrome', port=8081, host='localhost')




