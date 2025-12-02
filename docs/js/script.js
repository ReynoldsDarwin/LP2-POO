// ===== VARIABLES GLOBALES =====
const navbar = document.getElementById('navbar');
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
const scrollTopBtn = document.getElementById('scrollTopBtn');
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');

// ===== SMOOTH SCROLL Y NAVEGACIÓN =====
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        
        // Si es el link de "Inicio", ir directamente al top
        if (targetId === '#inicio') {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        } else {
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                // Calcular offset del navbar
                const navbarHeight = navbar.offsetHeight;
                const targetPosition = targetSection.offsetTop - navbarHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        }

        // Cerrar menú móvil si está abierto
        if (window.innerWidth <= 768) {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
        }
    });
});

// ===== MENÚ MÓVIL TOGGLE =====
navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    navToggle.classList.toggle('active');
});

// Cerrar menú al hacer click fuera de él
document.addEventListener('click', (e) => {
    if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
        navMenu.classList.remove('active');
        navToggle.classList.remove('active');
    }
});

// ===== SCROLL HANDLER OPTIMIZADO (COMBINADO) =====
let ticking = false;

window.addEventListener('scroll', () => {
    if (!ticking) {
        window.requestAnimationFrame(() => {
            const currentScroll = window.pageYOffset;
            
            // Navbar scroll effect
            if (currentScroll > 100) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
            
            // Scroll to top button
            if (currentScroll > 500) {
                scrollTopBtn.classList.add('show');
            } else {
                scrollTopBtn.classList.remove('show');
            }
            
            // Highlight active nav link
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                if (currentScroll >= sectionTop - 200) {
                    current = section.getAttribute('id');
                }
            });
            
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${current}`) {
                    link.classList.add('active');
                }
            });
            
            // Parallax effect en hero
            const hero = document.querySelector('.hero');
            if (hero && currentScroll < window.innerHeight) {
                hero.style.transform = `translateY(${currentScroll * 0.5}px)`;
                hero.style.opacity = 1 - (currentScroll / window.innerHeight);
            }
            
            ticking = false;
        });
        ticking = true;
    }
});

// ===== BOTÓN SCROLL TO TOP =====
scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// ===== ANIMACIÓN DE ELEMENTOS AL HACER SCROLL (INTERSECTION OBSERVER) =====
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

// Observar todos los elementos con la clase fade-in-element
document.querySelectorAll('.fade-in-element').forEach(element => {
    observer.observe(element);
});

// ===== ANIMACIÓN HOVER EN CARDS ABOUT CON EFECTO 3D =====
document.querySelectorAll('.about-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = rect.width / 5;
        const centerY = rect.height / 5;
        
        const rotateX = (y - centerY) / 150;
        const rotateY = (centerX - x) / 150;
        
        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-5px)`;
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
    });
});

// ===== ANIMACIÓN DE HOVER EN CARDS DE TEMAS CON EFECTO 3D =====
document.querySelectorAll('.card-link').forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = (y - centerY) / 10;
        const rotateY = (centerX - x) / 10;
        
        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px)`;
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
    });
});

// ===== PRELOAD - SCROLL SUAVE AL CARGAR =====
window.addEventListener('load', () => {
    // Si hay un hash en la URL, hacer scroll suave a esa sección
    if (window.location.hash) {
        setTimeout(() => {
            const targetSection = document.querySelector(window.location.hash);
            if (targetSection) {
                const navbarHeight = navbar.offsetHeight;
                const targetPosition = targetSection.offsetTop - navbarHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        }, 100);
    }
});

// ===== NAVEGACIÓN CON TECLADO (ACCESIBILIDAD) =====
// Permitir activar el toggle del menú con Enter o Space
navToggle.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        navMenu.classList.toggle('active');
        navToggle.classList.toggle('active');
    }
});

// ===== DETECCIÓN DE SCROLL HACIA ARRIBA/ABAJO =====
let lastScrollTop = 0;
window.addEventListener('scroll', () => {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    // Puedes usar esta lógica en el futuro para ocultar/mostrar el navbar
    if (scrollTop > lastScrollTop) {
        // Scrolling down
        // navbar.style.transform = 'translateY(-100%)';  // Opcional: ocultar navbar
    } else {
        // Scrolling up
        // navbar.style.transform = 'translateY(0)';  // Opcional: mostrar navbar
    }
    
    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
}, false);

// ===== CARRUSEL DE PROYECTOS =====
const carouselSlides = document.querySelectorAll('.carousel-slide');
const prevBtn = document.querySelector('.carousel-control.prev');
const nextBtn = document.querySelector('.carousel-control.next');
const indicators = document.querySelectorAll('.indicator');

let currentSlide = 0;
const totalSlides = carouselSlides.length;

// Función para mostrar slide
function showSlide(index) {
    // Asegurar que el índice esté en rango
    if (index >= totalSlides) {
        currentSlide = 0;
    } else if (index < 0) {
        currentSlide = totalSlides - 1;
    } else {
        currentSlide = index;
    }

    // Ocultar todos los slides
    carouselSlides.forEach(slide => {
        slide.classList.remove('active');
    });

    // Mostrar slide actual
    carouselSlides[currentSlide].classList.add('active');

    // Actualizar indicadores
    indicators.forEach((indicator, i) => {
        indicator.classList.remove('active');
        if (i === currentSlide) {
            indicator.classList.add('active');
        }
    });
}

// Navegación con flechas
if (prevBtn && nextBtn) {
    prevBtn.addEventListener('click', () => {
        showSlide(currentSlide - 1);
    });

    nextBtn.addEventListener('click', () => {
        showSlide(currentSlide + 1);
    });
}

// Navegación con indicadores
indicators.forEach((indicator, index) => {
    indicator.addEventListener('click', () => {
        showSlide(index);
    });
});

// Navegación con teclado (flechas)
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
        showSlide(currentSlide - 1);
    } else if (e.key === 'ArrowRight') {
        showSlide(currentSlide + 1);
    }
});

//Auto-play opcional (descomenta si quieres que cambie automáticamente)
let autoplayInterval = setInterval(() => {
    showSlide(currentSlide + 1);
}, 4000); // Cambia cada 4 segundos

// Pausar autoplay al hover (si está activado)
const carouselContainer = document.querySelector('.carousel-container');
if (carouselContainer) {
    carouselContainer.addEventListener('mouseenter', () => {
        clearInterval(autoplayInterval);
    });
    
    carouselContainer.addEventListener('mouseleave', () => {
        autoplayInterval = setInterval(() => {
            showSlide(currentSlide + 1);
        }, 4000);
    });
}


// ===== CONSOLE LOG DE BIENVENIDA =====
console.log('%c🐍 LP2 - POO en Python', 'font-size: 20px; color: #00ff99; font-weight: bold;');
console.log('%cDesarrollado por Darwin Reynolds', 'font-size: 14px; color: #a0aec0;');
console.log('%cRepositorio: https://github.com/ReynoldsDarwin/LP2-POO', 'font-size: 12px; color: #00ff99;');
console.log('%c✨ Sitio optimizado y accesible', 'font-size: 11px; color: #6ee7b7; font-style: italic;');
