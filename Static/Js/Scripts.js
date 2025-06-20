document.addEventListener('DOMContentLoaded', () => {
    console.log('Dashboard cargado!');
    
    // Efecto al hacer clic en tarjetas
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('click', () => {
            card.style.boxShadow = '0 0 15px rgba(0, 0, 255, 0.2)';
            setTimeout(() => {
                card.style.boxShadow = '';
            }, 300);
        });
    });
});
