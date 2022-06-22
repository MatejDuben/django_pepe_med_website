var navbar = document.querySelector('.nav-bar-wrapper');
var navbarFix = document.querySelector('.nav-bar-wrapper-fix');
let scrollTopBtn = document.querySelector('.button_top');

let responsiveLogo = document.getElementById('logo');

window.onscroll = function (){
  if (window.pageYOffset > 200) {
    gsap.to(".nav-bar-wrapper-fix", {y: "100px", duration: 0.4});
    //responsive logo
    
  }  
  else {
    gsap.to(".nav-bar-wrapper-fix", {y: "-100px", duration: 0.4});
    //responsive logo
  
  }
  //scropp to top btn
  if (window.pageYOffset > 500){
    scrollTopBtn.style.display = "block";
  }
  else{
    scrollTopBtn.style.display = "none";
  }
}


/*
***** scrroll btn 
*/
//SET scroll to top button
scrollTopBtn.addEventListener('click', (e)=>{
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
})

