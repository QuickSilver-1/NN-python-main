const form = document.getElementById('model');

function models (event) {
    event.preventDefault();

    const models = form.querySelectorAll('[name="model"]');
    console.log(models);

    for (let i = 0; i < models.length; i++) {
        if (models[i].checked) {
            nn = models[i].value;
        };
    };

    console.log(nn);

        eel.load_model_nn(nn);
    };

form.addEventListener('submit', models);
