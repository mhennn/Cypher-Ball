window.addEventListener('DOMContentLoaded', (event) => {
    const form = document.getElementById('requestForm');
    const editableTitle = document.getElementById('user-text');
    const hiddenInput = document.getElementById('hidden-answer');

    if (form) {
        form.onsubmit = function (e) {
            const content = editableTitle.innerText.trim();

            if (content === "") {
                e.preventDefault(); // Stop the form
                editableTitle.style.borderBottom = "2px solid red";
                alert("Input data, please???");
                return false;
            }

            hiddenInput.value = content;
        };

        editableTitle.addEventListener('input', () => {
            editableTitle.style.borderBottom = "1px solid white";
        });
    }
});