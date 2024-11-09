//Header
const navBar = document.querySelector('header');
window.onscroll = () => {
  if(window.scrollY > 100){
    navBar.classList.add('bg-color-primary-dark');
    navBar.classList.add('border-b');
    navBar.classList.add('bg-color-gray');
  }
  else{
    navBar.classList.remove('bg-color-primary-dark');
    navBar.classList.remove('border-b');
    navBar.classList.remove('bg-color-gray');
  }
}


//Mobile Menu
const hamburger = document.querySelector('#hamburger-icon');
const menu = document.querySelector('#menu');
const hlink = document.querySelector('#hlink');
const faSolid = document.querySelector('.fa-solid');

hamburger.addEventListener('click', () => {
  menu.classList.toggle('hidden');
  faSolid.classList.toggle('fa-xmark');
})

hlink.forEach(() => {
  hlink.addEventListener("click", () => {
    menu.classList.toggle('hidden');
    faSolid.classList.toggle('fa-xmark');
  })
});


