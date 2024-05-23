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
            const pokemonType = poke.types[0].type.name;
            containerPokemons.innerHTML += 
            `<div class="pokemon type-${pokemonType}">
            <img src="${poke.sprites.versions["generation-v"]["black-white"].animated.front_default}"/>

            <h4>${poke.name}</h4>

            <div class="types">
                ${poke.types.map(item => `<span class="type ${item.type.name}">${item.type.name}</span>`).join('')}
            </div>
            <br>
            `
        })
    }
}

captarPokemons()
