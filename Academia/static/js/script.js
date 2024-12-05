function modificarTreino(treinoId) {
    // Redireciona para a página de detalhes do treino, passando o treinoId como parâmetro na URL
    window.location.href = `/user/?treino_id=${treinoId}`;
}

function voltarParaTreinos() {
    // Remove o treino_id da URL e retorna à lista de treinos
    window.location.href = '/user/';
}

function toggleForm(formId) {
    const form = document.getElementById(formId);
    if (form) {
        // Exibe ou oculta o formulário com base no estado atual
        form.style.display = form.style.display === 'none' || form.style.display === '' ? 'block' : 'none';
    }
}
