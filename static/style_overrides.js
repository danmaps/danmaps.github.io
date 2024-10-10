document.querySelectorAll('iframe').forEach((iframe) => {
    iframe.onload = function() {
        const h1 = iframe.contentDocument.querySelector('.observablehq-root h1');
        if (h1) {
            h1.style.display = 'none';
        }
    };
});