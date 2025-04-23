document.addEventListener('DOMContentLoaded', function() {
    const areaBun = document.querySelector('map[name="image-map"] area:nth-child(3)');
    const leftSection = document.getElementById('left-section');
    const rightSection = document.getElementById('right-section');
    const title2 = document.querySelector('.title-2');
    const tapTheMap = document.querySelector('.tap-the-map');
    
    let colorsChanged = false;
    
    areaBun.addEventListener('click', function(e) {
        e.preventDefault();
        
        if (colorsChanged) {
            leftSection.style.backgroundColor = '#F7F3E2';
            rightSection.style.backgroundColor = '#E7D4C6';
            leftSection.style.color = '#2C351B';
            rightSection.style.color = '#2C351B';
        } else {
            leftSection.style.backgroundColor = '#C49855';
            rightSection.style.backgroundColor = '#FF6A3B';
            leftSection.style.color = '#2C351B';
            rightSection.style.color = '#2C351B';
        }
        
        colorsChanged = !colorsChanged;
    });

    const image = document.querySelector('.image-icon');
    const areaCoffee = document.querySelector('map[name="image-map"] area:nth-child(2)');
    
    areaCoffee.addEventListener('click', function(e) {
        e.preventDefault();
        
        image.classList.add('shake-animation');
        
        setTimeout(() => {
            image.classList.remove('shake-animation');
        }, 500);
    });

    const areaBook = document.querySelector('map[name="image-map"] area:nth-child(4)');
    const body = document.body;
    const title = document.querySelector('.title-2');
    const listItems = document.querySelectorAll('.tap-the-map li');
    
    let isGlowing = false;

    areaBook.addEventListener('click', function(e) {
        e.preventDefault();
        
        if (!isGlowing) {
            
            if (colorsChanged) {
                image.classList.add('image-glow-white');
                title.classList.add('text-glow-white');
                listItems.forEach(item => item.classList.add('text-glow-white'));
            } else {
                image.classList.add('image-glow-black');
                title.classList.add('text-glow-black');
                listItems.forEach(item => item.classList.add('text-glow-black'));
            }
        } else {
            image.classList.remove('image-glow-white', 'image-glow-black');
            title.classList.remove('text-glow-white', 'text-glow-black');
            listItems.forEach(item => item.classList.remove('text-glow-white', 'text-glow-black'));
        }
        
        isGlowing = !isGlowing;
    });

    const areaStrawberry = document.querySelector('map[name="image-map"] area:nth-child(5)');
    const modal = document.getElementById('modal');
    const modalContent = document.querySelector('.modal-content');
    const closeModalBtn = document.querySelector('.close-modal');

    areaStrawberry.addEventListener('click', function(e) {
        e.preventDefault();
        
        if (colorsChanged) {
            modalContent.classList.add('dark-theme');
        } else {
            modalContent.classList.remove('dark-theme');
        }
        
        modal.style.display = 'flex';
    });

    closeModalBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });

    const areaPlate = document.querySelector('map[name="image-map"] area:nth-child(6)');
    const hiddenText = document.getElementById('hidden_content');

    areaPlate.addEventListener('click', function(e) {
        e.preventDefault();
        hiddenText.classList.toggle('hidden');
        hiddenText.classList.toggle('visible');
    });

});
