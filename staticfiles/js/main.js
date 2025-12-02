document.addEventListener('DOMContentLoaded', function(){
  // Fade-in Hero
  document.querySelectorAll('.fade-in').forEach((el,i)=>{
    el.style.animationDelay = (i*120)+'ms';
    el.classList.add('fade-in');
  });

  // Smooth scroll
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener('click', function(e){
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if(target) target.scrollIntoView({behavior:'smooth', block:'start'});
    });
  });

  // Fade-in-up on scroll
  const faders = document.querySelectorAll('.fade-in-up');
  const appearOptions = { threshold: 0.1, rootMargin: "0px 0px -50px 0px" };
  const appearOnScroll = new IntersectionObserver(function(entries, observer){
    entries.forEach(entry=>{
      if(!entry.isIntersecting) return;
      entry.target.classList.add('show');
      observer.unobserve(entry.target);
    });
  }, appearOptions);
  faders.forEach(fader => appearOnScroll.observe(fader));
});

// Parallax Hero Background
window.addEventListener('scroll', function(){
  const bg = document.querySelector('.hero-bg');
  if(bg){
    let offset = window.pageYOffset;
    bg.style.transform = 'translateY(' + offset * 0.4 + 'px)';
  }
});
