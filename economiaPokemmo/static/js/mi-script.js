/* Selectores */
const ivs = document.querySelector('#ivs');
const precio = document.querySelector('#precio');
const cPokes = document.querySelector('.cPokes')
const pPokes = document.querySelector('.pPokes')
const cBra = document.querySelector('.cBra')
const pBra = document.querySelector('.pBra')
const cBall = document.querySelector('.cBall')
const pBall = document.querySelector('.pBall')
const cBreed = document.querySelector('.cBreed')
const pBreed =document.querySelector('.pBreed')
const rarity = document.querySelector('#rarity')
const pTotal = document.querySelector('.pTotal')
const btn=document.querySelector('.breed__form--button');

/* Variables globales */
const precio_cintas=10000;
const precio_pokebolas=200;

/* Funciones */
function calculo() {
  let precio_base=parseInt(precio.value)
  let ivs_base = parseInt(ivs.value)
  let pokes_base=2**(ivs_base-1);
  let precioTotalPokes=precio_base*pokes_base;
  let cantidad_total=pokes_base*2;
  let cantidad_cintas=cantidad_total-2;
  let precioTotalCintas=precio_cintas*cantidad_cintas;
  let cantidad_breed=(pokes_base/2)
  let precioTotalBreed=cantidad_breed*5000
  let cantidad_pokebolas=cantidad_total-1;
  let precioTotalPokebolas=precio_pokebolas*cantidad_pokebolas;
  let rareza;
  let total;
  if (rarity.value > 0) {
    rareza= (ivs_base-1)*21000;
    precioTotalBreed= precioTotalBreed + rareza
  }else{
    rareza = 0;
  }
  if (ivs.value>=1 && precio_base >=1){
    total=precioTotalCintas+precioTotalPokebolas+precioTotalPokes+rareza;
  }else {
    pokes_base = 0;
    precio_base = 0;
    precioTotalPokes= 0;
    cantidad_total = 0;
    cantidad_cintas = 0;
    precioTotalCintas = 0;
    cantidad_breed = 0;
    precioTotalBreed = 0;
    cantidad_pokebolas = 0;
    precioTotalPokebolas = 0;
    total=precioTotalCintas+precioTotalPokebolas+precioTotalPokes;
  }
  cPokes.innerText = pokes_base;
  pPokes.innerText = precioTotalPokes;
  cBra.innerText = cantidad_cintas;
  pBra.innerText = precioTotalCintas;
  cBreed.innerText = cantidad_breed;
  pBreed.innerText = precioTotalBreed;
  cBall.innerText = cantidad_pokebolas;
  pBall.innerText = precioTotalPokebolas;
  pTotal.innerText = total
};
/*Acciones*/
btn.addEventListener('click',calculo)