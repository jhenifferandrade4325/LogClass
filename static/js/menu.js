// Componente Menu

document.addEventListener('DOMContentLoaded', async function () {
    try {
        const codMenu = await fetch('/static/menu-home/menu-home.html');
        // const codMenu = await fetch('./templates/menu-home.html');
        if (!codMenu.ok) {
            throw new Error('Arquivo não encontrado no servidor.');
        }
        const menu = await codMenu.text();
        document.querySelector('.container-menu').innerHTML = menu;
        initMenuMobile();
    } catch (error) {
        console.error('Erro ao carregar o menu: ', error);
    }
});


// Função para inicializar os eventos do menu mobile
const initMenuMobile = () => {

    const  btnMobile = document.querySelector('#btn-mobile');
    if (!btnMobile) {
        console.error('#btn-mobile não encontrado');
        return;
    }
    const toggleMenu = (event) => {
        // BL 01
        if (event.type === 'touchstart') event.preventDefault();
    
        // Adicionar a classe acttive, caso não tenha.
        // Remover a classe acttive, caso tenha
        // BL 02
        const nav = document.getElementById('nav'); 
        nav.classList.toggle('active');
        const active = nav.classList.contains('active');

        // BL 03
        event.currentTarget.setAttribute('aria-expanded', active);
        if(active){
            event.currentTarget.setAttribute('aria-label', 'Fechar Menu');
        }else{
            event.currentTarget.setAttribute('aria-label', 'Abrir Menu');
    
        }
    }
    
    btnMobile.addEventListener('click', toggleMenu);
    btnMobile.addEventListener('touchstart', toggleMenu);
}

