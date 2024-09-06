document.addEventListener('DOMContentLoaded', function() {
    const itens = document.querySelectorAll('.carrossel');
    let currentIndex = 0;
  
    function showItem(index) {
      itens.forEach(item => {
        item.style.transform = `translateX(-${index * 100}%)`;
      });
    }
  
    function nextItem() {
      if (currentIndex < itens.length - 1) {
        currentIndex++;
      } else {
        currentIndex = 0;
      }
      showItem(currentIndex);
    }
  
    function prevItem() {
      if (currentIndex > 0) {
        currentIndex--;
      } else {
        currentIndex = itens.length - 1;
      }
      showItem(currentIndex);
    }
  
    document.querySelector('.anterior').addEventListener('click', prevItem);
    document.querySelector('.próximo').addEventListener('click', nextItem);
  });