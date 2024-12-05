// script.js

function toggleForm() {
    var form = document.getElementById('formCriarTreino');
    var mensagemSemTreinos = document.getElementById('mensagemSemTreinos');

    if (form.style.display === 'none' || form.style.display === '') {
        form.style.display = 'block';
        if (mensagemSemTreinos) {
            mensagemSemTreinos.style.display = 'none';
        }
    } else {
        form.style.display = 'none';
        if (mensagemSemTreinos) {
            mensagemSemTreinos.style.display = 'block';
        }
    }
}
