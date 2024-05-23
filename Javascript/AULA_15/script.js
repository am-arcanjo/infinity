//Lembrete: se for uma classe usamos o '.' na frente e se for um id usamos '#'
//Por convenção, para indicar valores fixos, colocamos letra maiúscula

const BASE_API_URL = "https://pokeapi.co/api/v2"

const containerPokemons = document.querySelector(".pokemons");
const pokemonsTypeSelect = document.querySelector(".pokemonsTypeSelect");
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
            let pokemonTypes = poke.types.map(t => t.type.name);
            let pokemonTypeClass = pokemonTypes.join('');

            containerPokemons.innerHTML += 
            `<div class="pokemon type-${pokemonTypeClass}">
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

function filtrarPokemonsPorTipo() {
    fetch(`${BASE_API_URL}/pokemon?limit=40/${pokemonsTypeSelect}`)
    .then((resposta) => resposta.json())
    .then(dado => {
        pokemons = dado.results
    })
}

captarPokemons()
