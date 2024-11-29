// Função que move o boneco conforme o movimento do mouse
document.addEventListener('mousemove', function(event) {
    const boneco = document.getElementById('boneco');
    
    // Atualiza a posição do boneco para seguir o mouse
    boneco.style.left = event.pageX - boneco.offsetWidth / 2 + 'px';
    boneco.style.top = event.pageY - boneco.offsetHeight / 2 + 'px';
});
