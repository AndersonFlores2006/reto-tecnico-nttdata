document.addEventListener('DOMContentLoaded', () => {
    const API_URL = 'http://localhost:8000/api/personas';
    const listaEl = document.getElementById('lista');
    const loadingEl = document.getElementById('loading');
    const errorEl = document.getElementById('error');
    const btnNuevas = document.getElementById('btn-nuevas');

    async function cargarPersonas() {
        loadingEl.classList.remove('hidden');
        errorEl.classList.add('hidden');
        listaEl.innerHTML = '';

        try {
            const response = await fetch(API_URL);
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }
            const data = await response.json();
            mostrarPersonas(data.personas);
        } catch (err) {
            console.error(err);
            errorEl.textContent = 'No se pudieron cargar las personas. Asegurate de que el backend este corriendo en http://localhost:8000';
            errorEl.classList.remove('hidden');
        } finally {
            loadingEl.classList.add('hidden');
        }
    }

    btnNuevas.addEventListener('click', cargarPersonas);

    function mostrarPersonas(personas) {
        listaEl.innerHTML = '';
        personas.forEach(persona => {
            const card = document.createElement('article');
            card.className = 'card';
            card.innerHTML = `
                <img src="${persona.fotografia}" alt="Foto de ${persona.nombre}" class="foto">
                <div class="info">
                    <h2>${persona.nombre}</h2>
                    <p><strong>Genero:</strong> ${persona.genero}</p>
                    <p><strong>Ubicacion:</strong> ${persona.ubicacion}</p>
                    <p><strong>Email:</strong> <a href="mailto:${persona.email}">${persona.email}</a></p>
                    <p><strong>Fecha de nacimiento:</strong> ${formatearFecha(persona.fecha_nacimiento)}</p>
                </div>
            `;
            listaEl.appendChild(card);
        });
    }

    function formatearFecha(fechaISO) {
        if (!fechaISO) return 'Desconocida';
        const fecha = new Date(fechaISO);
        return fecha.toLocaleDateString('es-ES', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    }

    cargarPersonas();
});
