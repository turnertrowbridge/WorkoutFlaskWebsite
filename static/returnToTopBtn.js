const returnToTopBtn = document.getElementById('return-to-top-btn');

window.addEventListener('scroll', () => {
    if (window.scrollY > 0) {
        returnToTopBtn.style.display = 'block';
    } else {
        returnToTopBtn.style.display = 'none';
    }
});

returnToTopBtn.addEventListener('click', () => {
    document.getElementById('top').scrollIntoView({ behavior: 'smooth' });
});
