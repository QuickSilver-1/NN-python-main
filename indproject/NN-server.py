import numpy as np
from tensorflow import keras
#from keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D
#from keras.datasets import mnist
#import matplotlib.pyplot as plt
from PIL import Image
import socket
import json


def go(data):

    data = np.array(data)
    data.shape = (392, 392)
    data = Image.fromarray(data)
    data = data.resize((28, 28), Image.ANTIALIAS)

    img = np.expand_dims(data, axis=0)
    img = img / 255
    if model == 'defoult':
        answer = neuralNet_defoult.predict(img)
        answer = list(map(lambda x: round(x * 100, 2), answer[0]))
        return answer
    else:
        answer = neuralNet_better.predict(img)
        answer = list(map(lambda x: round(x * 100, 2), answer[0]))
        return answer


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
#     neuralNet_defoult.fit(train_images, train_answer, batch_size=128,
#                   epochs=epochs, validation_split=0.2)
#     neuralNet_defoult.evaluate(test_images, test_answer)
#     neuralNet_defoult.fit(train_images, train_answer, batch_size=128,
#                   epochs=epochs, validation_split=0.2)
#     neuralNet_better.evaluate(test_images, test_answer)
#     neuralNet_better.save('better.h5')
#     neuralNet_defoult.save('defoult.h5')
#     score = neuralNet_defoult.evaluate(test_images, test_answer, verbose=0)
#     print('Потери на тесте:', score[0])
#     print('Точность на тесте:', score[1])
#     score = neuralNet_better.evaluate(test_images, test_answer, verbose=0)
#     print('Потери на тесте:', score[0])
#     print('Точность на тесте:', score[1])

# def make_defoultnn(neirons):
#     neirons = int(neirons)
#     neuralNet_defoult = keras.Sequential([
#         Flatten(input_shape=(28, 28, 1)),
#         Dense(neirons, activation='relu'),
#         Dense(10, activation='softmax')])
#     neuralNet_defoult.compile(optimizer='adam',
#                       loss='categorical_crossentropy',
#                       metrics=['accuracy'])
#     neuralNet_defoult.save('defoult')


# def make_betternn():
#     neuralNet_better = keras.Sequential([
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
#     neuralNet_better.compile(optimizer='adam',
#                       loss='categorical_crossentropy',
#                       metrics=['accuracy'])
#     neuralNet_better.save('better')


# make_defoultnn(256)
# make_betternn()
# learning(30)


neuralNet_defoult = keras.models.load_model('defoult.h5')
neuralNet_better = keras.models.load_model('better.h5')
test = np.array([[0]*28]*28)
test = np.expand_dims(test, axis=0)
neuralNet_defoult.predict(test)
neuralNet_better.predict(test)
model = 'defoult'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname(socket.gethostname()), 1025))
server.listen(4)
print('Waiting...')


while True:
    try:
        user, adress = server.accept()
        print('connect')
        while True:
            data = user.recv(524288)
            if data == '':
                print('Waiting...')
                break
            command, data = json.loads(data)
            if command == 'image':
                answer = go(data)
                user.send(json.dumps(answer).encode('utf-8'))
            else:
                model = data
    except ConnectionResetError:
        print('Waiting...')
        continue










