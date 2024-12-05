function modificarTreino(treinoId) {
    // Oculta todos os treinos e exibe os detalhes do treino selecionado
    document.getElementById('listaTreinos').style.display = 'none';
    window.location.href = `/user/?treino_id=${treinoId}`;
}

function voltarParaTreinos() {
    // Redireciona para a página de treinos sem um treino selecionado
    window.location.href = '/user/';
}

function toggleForm(formId) {
    var form = document.getElementById(formId);
    if (form.style.display === 'none' || form.style.display === '') {
        form.style.display = 'block';
    } else {
        form.style.display = 'none';
    }
}
