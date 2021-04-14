var modals = document.getElementById('simpleModals');
var modalBtns = document.getElementById('modalBtns');
var closeBtns = document.getElementsByClassName('closeBtns')[0];


modalBtns.addEventListener('click', openModal);
closeBtns.addEventListener('click', closeModal);

window.addEventListener('click', outsideClick);

function openModal(){
  modals.style.display = 'block';
}
 
function closeModal(){
  modals.style.display = 'none';
}
 
function outsideClick(e){
    if(e.target == modals){
    modals.style.display = 'none';
}
}