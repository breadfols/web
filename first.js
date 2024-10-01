const coffeeLinks = document.querySelectorAll('.coffee-link');

coffeeLinks.forEach(link => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    const linkId = link.id; 
    const infoBlockId = linkId.replace('-link', '-info'); 
    const infoBlock = document.getElementById(infoBlockId); 

    const allInfoBlocks = document.querySelectorAll('.coffee-info');
    allInfoBlocks.forEach(block => {
      block.style.display = 'none'; 
    });
    
    infoBlock.style.display = 'block';
  });
});