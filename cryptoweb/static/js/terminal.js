document.addEventListener('DOMContentLoaded', function() {
    const terminal = document.getElementById('terminal');
    const commandInput = document.getElementById('commandInput');
    const runCommand = document.getElementById('runCommand');

    runCommand.addEventListener('click', function() {
        const command = commandInput.value.trim();
        if (command) {
            const output = document.createElement('div');
            if (command.startsWith('md5 ')) {
                const textToHash = command.slice(4);
                const hash = md5(textToHash);
                output.textContent = `> ${command}\n${hash}`;
            } else {
                output.textContent = `> ${command}\nComando no reconocido.`;
            }
            terminal.appendChild(output);
            commandInput.value = '';
        }
    });

    function md5(string) {
        return crypto.subtle.digest('MD5', new TextEncoder().encode(string)).then(buffer => {
            return Array.from(new Uint8Array(buffer)).map(b => b.toString(16).padStart(2, '0')).join('');
        });
    }
});