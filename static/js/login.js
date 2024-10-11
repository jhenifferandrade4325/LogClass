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

//----------------------------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function() {
    // Botões e seções principais
    const signupBtn = document.getElementById("signup-btn");
    const loginBtn = document.getElementById("login-btn");
    const introSection = document.getElementById("intro-section");
    const registerSection = document.getElementById("register-section");
    const loginSection = document.getElementById("login-section");

    // Seções de cadastro
    const alunoRegisterBtn = document.getElementById("aluno-register-btn");
    const professorRegisterBtn = document.getElementById("professor-register-btn");
    const registerAluno = document.getElementById("register-aluno");
    const registerProfessor = document.getElementById("register-professor");
    const connectBoxRegister = document.querySelector("#register-section .connect-box");

    // Seções de login
    const alunoLoginBtn = document.getElementById("aluno-login-btn");
    const professorLoginBtn = document.getElementById("professor-login-btn");
    const loginAluno = document.getElementById("login-aluno");
    const loginProfessor = document.getElementById("login-professor");
    const connectBoxLogin = document.getElementById("connect-login");

    // Função para exibir a tela de cadastro
    signupBtn.addEventListener("click", function() {
        introSection.style.display = "none";
        registerSection.style.display = "flex";
        connectBoxRegister.style.display = "block";
        registerAluno.style.display = "none";
        registerProfessor.style.display = "none";
    });

    function exibirLogin(){
        introSection.style.display = "none";
        loginSection.style.display = "block";
        connectBoxLogin.style.display = "block";
        loginAluno.style.display = "none";
        loginProfessor.style.display = "none";
    }

    // Função para exibir a tela de login
    loginBtn.addEventListener("click", function() {
        exibirLogin()
    });


    // Função para exibir o cadastro do aluno
    alunoRegisterBtn.addEventListener("click", function() {
        connectBoxRegister.style.display = "none";
        registerAluno.style.display = "block";
        registerProfessor.style.display = "none";
    });

    // Função para exibir o cadastro do professor
    professorRegisterBtn.addEventListener("click", function() {
        connectBoxRegister.style.display = "none";
        registerProfessor.style.display = "block";
        registerAluno.style.display = "none";
    });

    function exibirLoginAluno(){
        connectBoxLogin.style.display = "none";
        loginAluno.style.display = "block";
        loginProfessor.style.display = "none";
    };

    // Função para exibir o login do aluno
    alunoLoginBtn.addEventListener("click", function() {
        exibirLoginAluno();
    });

    function exibirLoginProfessor(){
        connectBoxLogin.style.display = "none";
        loginProfessor.style.display = "block";
        loginAluno.style.display = "none";
    };

    // Função para exibir o login do professor
    professorLoginBtn.addEventListener("click", function() {
        exibirLoginProfessor();
    });


    // Função para voltar à tela de seleção no cadastro
    document.querySelectorAll("#voltar-register").forEach(button => {
        button.addEventListener("click", function() {
            registerSection.style.display = "flex";
            connectBoxRegister.style.display = "block";
            registerAluno.style.display = "none";
            registerProfessor.style.display = "none";
        });
    });

    // Função para voltar à tela de seleção no login
    document.querySelectorAll("#voltar-login").forEach(button => {
        button.addEventListener("click", function() {
            loginSection.style.display = "block";
            connectBoxLogin.style.display = "block";
            loginAluno.style.display = "none";
            loginProfessor.style.display = "none";
        });
    });
});
