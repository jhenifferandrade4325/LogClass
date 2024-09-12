// Código para o input de TROCAR TURMAS ---------------------------------------------------

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
// --------------------------------------------------------------------------------------

// Código para trocar a Tela 01 para Tela 02
document.addEventListener("DOMContentLoaded", function() {
    const alunoBtn = document.getElementById("aluno-btn");
    const professorBtn = document.getElementById("professor-btn");
    const loginAluno = document.getElementById("login-aluno");
    const loginProfessor = document.getElementById("login-professor");
    const connectBox = document.querySelector(".connect-box");
    const voltarAluno = document.getElementById("voltar-aluno");
    const voltarProfessor = document.getElementById("voltar-professor");

    professorBtn.addEventListener("click", function() {
        connectBox.style.display = "none"; // Esconde a tela de seleção
        loginProfessor.style.display = "block"; // Exibe a tela de login do professor
        loginAluno.style.display = "none"; // Garante que a tela de login do aluno esteja oculta
    });

    alunoBtn.addEventListener("click", function() {
        if (loginAluno.style.display === "block") {
            alert("Você já está na página de cadastro do aluno");
        } else {
            loginProfessor.style.display = "none"; // Garante que a tela de login do professor esteja oculta
            loginAluno.style.display = "block"; // Exibe a tela de login do aluno
            connectBox.style.display = "none"; // Garante que a tela de seleção fique invisível
        }
    });

    voltarAluno.addEventListener("click", function() {
        loginProfessor.style.display = "none"; // Esconde a tela de login do professor
        loginAluno.style.display = "none"; // Esconde a tela de login do aluno
        connectBox.style.display = "block"; // Volta para a tela de seleção de tipo de conta
    });

    voltarProfessor.addEventListener("click", function() {
        loginProfessor.style.display = "none"; // Esconde a tela de login do professor
        loginAluno.style.display = "none"; // Esconde a tela de login do aluno
        connectBox.style.display = "block"; // Volta para a tela de seleção de tipo de conta
    });
});


document.getElementById("signup-btn").addEventListener("click", function() {
    document.getElementById("intro-section").style.display = "none";
    document.getElementById("login-section").style.display = "flex";
});








// document.addEventListener("DOMContentLoaded", function() {
//     const alunoBtn = document.getElementById("aluno-btn");
//     const professorBtn = document.getElementById("professor-btn");
//     const loginAluno = document.getElementById("login-aluno");
//     const loginProfessor = document.getElementById("login-professor");
//     const connectBox = document.querySelector(".connect-box");
//     const voltarAluno = document.getElementById("voltar-aluno");
//     const voltarProfessor = document.getElementById("voltar-professor");

//     professorBtn.addEventListener("click", function() {
//         connectBox.style.display = "none"; // Esconde a tela de seleção
//         loginProfessor.style.display = "block"; // Exibe a tela de login do professor
//         loginAluno.style.display = "none"; // Garante que a tela de login do aluno esteja oculta
//     });

//     alunoBtn.addEventListener("click", function() {
//         if (loginAluno.style.display === "block") {
//             alert("Você já está na página de cadastro do aluno");
//         } else {
//             loginProfessor.style.display = "none"; // Garante que a tela de login do professor esteja oculta
//             loginAluno.style.display = "block"; // Exibe a tela de login do aluno
//             connectBox.style.display = "none"; // Garante que a tela de seleção fique invisível
//         }
//     });

//     voltarAluno.addEventListener("click", function() {
//         loginProfessor.style.display = "none"; // Esconde a tela de login do professor
//         loginAluno.style.display = "none"; // Esconde a tela de login do aluno
//         connectBox.style.display = "block"; // Volta para a tela de seleção de tipo de conta
//     });

//     voltarProfessor.addEventListener("click", function() {
//         loginProfessor.style.display = "none"; // Esconde a tela de login do professor
//         loginAluno.style.display = "none"; // Esconde a tela de login do aluno
//         connectBox.style.display = "block"; // Volta para a tela de seleção de tipo de conta
//     });
// });


// document.getElementById("login-btn").addEventListener("click", function() {
//     document.getElementById("intro-section").style.display = "none";
//     document.getElementById("login-section").style.display = "flex";
// });


document.addEventListener("DOMContentLoaded", function() {
    const loginBtn = document.getElementById("login-btn");
    const loginExistenteSection = document.getElementById("login-existente-section");
    const introSection = document.getElementById("intro-section");
    const voltarLoginExistenteLink = document.getElementById("voltar-login-existente-link");
    const connectBox = document.querySelector(".connect-box");
    const alunoBtn = document.getElementById("aluno-btn");
    const professorBtn = document.getElementById("professor-btn");

    // Exibe a tela de login ao clicar em "IR PARA LOGIN"
    loginBtn.addEventListener("click", function() {
        introSection.style.display = "none";
        loginExistenteSection.style.display = "none";
    });



    // Volta para a tela de introdução ao clicar em "VOLTAR"
    voltarLoginExistenteLink.addEventListener("click", function() {
        loginExistenteSection.style.display = "none";
        introSection.style.display = "block";
    });
});

document.getElementById("login-btn").addEventListener("click", function() {
    document.getElementById("intro-section").style.display = "none";
    document.getElementById("login-section").style.display = "flex";
});
