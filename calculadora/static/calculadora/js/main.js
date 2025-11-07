document.addEventListener('DOMContentLoaded', function() {
    // Configurar formulario
    const calculadoraForm = document.getElementById('calculadoraForm');
    if (calculadoraForm) {
        calculadoraForm.addEventListener('submit', function(e) {
            e.preventDefault();
            ejecutarCalculadora();
        });
    }

    // Solo ejecutar cuando se presione calcular o se cambie el operador
    const operadorSelect = document.getElementById('operador');
    operadorSelect.addEventListener('change', function() {
        // Solo ejecutar si ambos campos tienen valores
        const x = document.getElementById('valor_x').value;
        const y = document.getElementById('valor_y').value;
        if (x !== '' && y !== '') {
            ejecutarCalculadora();
        }
    });

    // Remover ejecución automática al escribir en los inputs
    const inputs = document.querySelectorAll('input[type="number"]');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            // Ocultar resultado si falta algún campo
            const x = document.getElementById('valor_x').value;
            const y = document.getElementById('valor_y').value;
            if (x === '' || y === '') {
                document.getElementById('resultado').style.display = 'none';
            }
        });
    });
});

function ejecutarCalculadora() {
    const x = document.getElementById('valor_x').value;
    const y = document.getElementById('valor_y').value;
    const operador = document.getElementById('operador').value;
    
    // Validar que ambos campos tengan valores
    if (x === '' || y === '') {
        document.getElementById('resultado').style.display = 'none';
        return;
    }

    const resultadoDiv = document.getElementById('resultado');
    const contenidoDiv = document.getElementById('resultadoContent');

    // Mostrar loading
    contenidoDiv.innerHTML = '<div class="text-center">Calculando...</div>';
    resultadoDiv.style.display = 'block';

    // Generar código EXACTO como en tu calculadora.py original
    const codigo = `x = ${x};
y = ${y};
if (x ${operador} y) {
    z = x + y;
}`;

    fetch('/ejecutar/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({ codigo: codigo })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            mostrarResultado(data.resultado, x, y, operador, data.pasos);
        } else {
            contenidoDiv.innerHTML = `<div class="alert alert-danger">Error: ${data.error}</div>`;
        }
    })
    .catch(error => {
        contenidoDiv.innerHTML = `<div class="alert alert-danger">Error de conexión: ${error.message}</div>`;
    });
}

function mostrarResultado(variables, x, y, operador, pasos) {
    const contenidoDiv = document.getElementById('resultadoContent');
    const condicionCumplida = evaluarCondicion(parseInt(x), parseInt(y), operador);
    
    let html = '';
    
    // Mostrar ejecución paso a paso
    if (pasos && pasos.length > 0) {
        html += `
            <div class="mb-3">
                <h6>Ejecución paso a paso:</h6>
                <div class="border rounded p-3 bg-light">
                    ${pasos.map(paso => `<div class="mb-2">${paso}</div>`).join('')}
                </div>
            </div>
        `;
    }
    
    // Mostrar resultado final
    if (condicionCumplida) {
        html += `
            <div class="alert alert-success">
                <strong>Condición: x ${operador} y</strong><br>
                <strong>Resultado: VERDADERO</strong><br>
                Se ejecutó el bloque IF<br>
                z = x + y = ${x} + ${y} = ${variables.z}
            </div>
        `;
    } else {
        html += `
            <div class="alert alert-warning">
                <strong>Condición: x ${operador} y</strong><br>
                <strong>Resultado: FALSO</strong><br>
                No se ejecutó el bloque IF<br>
                La variable z no fue definida
            </div>
        `;
    }

    // Mostrar variables finales
    html += `
        <div class="mt-3">
            <h6>Variables finales:</h6>
            <pre class="bg-white p-2 border rounded">${JSON.stringify(variables, null, 2)}</pre>
        </div>
    `;

    contenidoDiv.innerHTML = html;
}

function evaluarCondicion(x, y, operador) {
    switch(operador) {
        case '>': return x > y;
        case '<': return x < y;
        case '==': return x == y;
        case '!=': return x != y;
        default: return false;
    }
}

function getCSRFToken() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
    return csrfToken ? csrfToken.value : '';
}

function limpiarFormulario() {
    document.getElementById('calculadoraForm').reset();
    document.getElementById('resultado').style.display = 'none';
}