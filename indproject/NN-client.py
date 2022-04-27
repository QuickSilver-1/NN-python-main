import eel
import socket
import json


eel.init('D:/prog/indproject/web')

@eel.expose
def send(data):
    data = ('image', data)
    client.send(json.dumps(data).encode('utf-8'))
    answer = client.recv(1024)
    answer = json.loads(answer)
    eel.write(answer)


@eel.expose
def load_model_nn(data):
    data = ('model', data)
    client.send(json.dumps(data).encode('utf-8'))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('5.3.133.77', 1025))


eel.start('main.html', size=(950, 700),
          mode='chrome', port=8081, host='localhost')


