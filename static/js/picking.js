document.querySelectorAll('.select-menu').forEach(menu => {
    const selectBtn = menu.querySelector('.select-btn');
    const options = menu.querySelectorAll('.option');
    const sBtnText = menu.querySelector('.sBtn-text');

    selectBtn.addEventListener('click', () => {
        menu.classList.toggle('active');
    });

    options.forEach(option => {
        option.addEventListener('click', () => {
            let selectedOption = option.querySelector('.option-text').innerText;
            sBtnText.innerText = selectedOption;
            menu.classList.remove('active');
        });
    });
});