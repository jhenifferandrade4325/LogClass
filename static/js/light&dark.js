// Evento que é disparado quando o conteúdo do DOM (estrutura HTML) é totalmente carregado
document.addEventListener('DOMContentLoaded', () => {
    // Verifica no localStorage se existe um tema salvo. Se não houver, define o tema padrão como 'light'
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Adiciona a classe correspondente ao tema (light ou dark) no corpo da página (body)
    document.body.classList.add(currentTheme);
  
    // Seleciona o botão de alternar tema usando o ID 'toggle-theme' e adiciona um evento de clique
    document.getElementById('toggle-theme').addEventListener('click', () => {
      // Verifica qual tema está atualmente aplicado no body (light ou dark)
      const newTheme = document.body.classList.contains('light') ? 'dark' : 'light';
  
      // Remove as classes de tema antigas ('light' e 'dark') para evitar conflito
      document.body.classList.remove('light', 'dark');
  
      // Adiciona a nova classe de tema ao body
      document.body.classList.add(newTheme);
  
      // Armazena o novo tema no localStorage para que a preferência do usuário seja mantida
      localStorage.setItem('theme', newTheme);
    });
});

