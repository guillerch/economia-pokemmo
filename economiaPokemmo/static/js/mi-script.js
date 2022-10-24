const ivs = document.querySelector('.ivs');
const precio = document.querySelector('.precio');
const resultado = document.querySelector('#resultado')
const btn=document.querySelector('.form__button');

btn.addEventListener('click',calculo)

function calculo() {
  let precio_cintas=10000
  let precio_pokebolas=200

  let pokes_base=2**(ivs.value-1)
  let cantidad_total=pokes_base*2
  let total;

  if (ivs.value>1) {
    total=((precio_cintas*(cantidad_total-2))+(precio_pokebolas*(cantidad_total-1))+(precio.value*pokes_base))
  } else {
    total = precio.value
  }
  resultado.innerText = "Costo total: "+ total
}