const form = document.getElementById('model'),
      training = document.getElementById('train');

async function train (event) {
    event.preventDefault();

    const epochs = training.querySelector('[name="epochs"]').value;
    await eel.learning(epochs);
};

function models (event) {
    event.preventDefault();

    const models = form.querySelector('[name="model"]').value,
          neirons = form.querySelector('[name="many"]').value;
    console.log(neirons);
    if (models == 'perceptron') {
        eel.make_defoultnn(neirons);
    };
};

form.addEventListener('submit', models);
training.addEventListener('submit', train);
