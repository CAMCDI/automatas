// JavaScript opcional para mejoras de UX
document.addEventListener('DOMContentLoaded', function() {
    const codeTextarea = document.getElementById('code');
    
    if (codeTextarea) {
        // Auto-expand textarea mientras se escribe
        codeTextarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });
        
        // Ejemplos clickeables
        const examples = document.querySelectorAll('.examples code');
        examples.forEach(example => {
            example.style.cursor = 'pointer';
            example.addEventListener('click', function() {
                codeTextarea.value = this.textContent;
                codeTextarea.focus();
            });
        });
    }
});