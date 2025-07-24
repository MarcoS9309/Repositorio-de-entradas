document.getElementById('mostrar-relato').addEventListener('click', function() {
    const microrelato = `
Abrió lentamente el viejo libro, cuyas páginas guardaban silencio desde hace décadas. 
Allí, escrita con una caligrafía temblorosa, encontró la última frase de su vida: 
“Siempre supiste cómo termina esto”.
`;

    document.getElementById('texto-relato').innerText = microrelato;
});
