/* Project specific Javascript goes here. */
function mask(input, func) {
    if (input.value.length < 1) return;

    const key = event.keyCode || event.charCode;
    if (key !== 8 && key !== 46) {
        func(input);
    }
}


function maskCPF(input) {
    input.value = input.value.replace(/\D/g, '')
        .replace(/^(\d{3})(\d)/, '$1.$2')
        .replace(/^(\d{3})\.(\d{3})(\d)/, '$1.$2.$3')
        .replace(/^(\d{3})\.(\d{3})\.(\d{3})(\d)/, '$1.$2.$3-$4')
        .substr(0, 14);
}

function maskZipCode(input) {
    input.value = input.value.replace(/\D/g, '')
        .replace(/^(\d{5})(\d)/, '$1-$2')
        .substr(0, 9);
}

function maskPhone(input) {
    input.value = input.value.replace(/\D/g, '')
        .replace(/^(\d{2})(\d)/g, '($1) $2')
        .replace(/(\d)(\d{4})$/, '$1-$2')
        .substr(0, 14);
}
