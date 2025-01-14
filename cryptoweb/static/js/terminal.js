document.addEventListener('DOMContentLoaded', function() {
    const terminal = document.getElementById('terminal');
    const commandInput = document.getElementById('commandInput');
    const runCommand = document.getElementById('runCommand');

    runCommand.addEventListener('click', function() {
        const command = commandInput.value;
        if (command) {
            const output = document.createElement('div');
            output.textContent = `> ${command}`;
            terminal.appendChild(output);
            commandInput.value = '';
            // Aquí puedes agregar la lógica para ejecutar el comando y mostrar el resultado en la terminal
        }
    });
});