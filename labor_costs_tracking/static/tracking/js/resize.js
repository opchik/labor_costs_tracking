document.addEventListener('DOMContentLoaded', function() {
    const tooltip = document.getElementById('tooltip');
    const tableCells = document.querySelectorAll('.styled-table td');

    tableCells.forEach(cell => {
        cell.addEventListener('mouseenter', function(event) {
            const content = this.getAttribute('title') || this.innerText;
            if (content != "") {
                tooltip.innerText = content;
                tooltip.style.left = `${event.pageX + 10}px`;
                tooltip.style.top = `${event.pageY + 10}px`;
                tooltip.style.display = 'block';
            }
        });

        cell.addEventListener('mouseleave', function() {
            tooltip.style.display = 'none';
        });
    });

    document.addEventListener('click', function(event) {
        if (!tooltip.contains(event.target) && !event.target.closest('.styled-table td')) {
            tooltip.style.display = 'none';
        }
    });
});