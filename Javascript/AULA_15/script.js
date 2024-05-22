//Lembrete: se for uma classe usamos o '.' na frente e se for um id usamos '#'
//Por convenção, para indicar valores fixos, colocamos letra maiúscula

const BASE_API_URL = "https://pokeapi.co/api/v2"


const containerPokemons = document.querySelector(".pokemons");
let pokemons = [];

function captarPokemons() {
    fetch(`${BASE_API_URL}/pokemon?limit=40`)
    .then((resposta) => resposta.json())
    .then(dado => {
        pokemons = dado.results

        captarPokemon()
    })
}

function captarPokemon() {
    for (let pokemon of pokemons) {
        fetch(pokemon.url)
        .then(resposta => resposta.json())
        .then(poke => {
            containerPokemons.innerHTML += 
            `<img src="${poke.sprites.versions["generation-v"]["black-white"].animated.front_default}"/>`
        })
    }
}

captarPokemons()