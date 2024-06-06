//Lembrete: se for uma classe usamos o '.' na frente e se for um id usamos '#'
//Por convenção, para indicar valores fixos, colocamos letra maiúscula

const shoppingCartQuantity = document.querySelector(".shopping-cart-quantity")
const containerCategories = document.querySelector(".categories")
const containerProducts = document.querySelector(".products-list")
const BASE_API = "https://fakestoreapi.com"

let shoppingCart = []
let products = []

async function getProducts() {
    try {
        let response = await fetch(`${BASE_API}/products`)
        let data = await response.json()

        products = data //TO-DO ter a referencia dos produtos para usar em filtragens

    } catch (error) {
        console.error(error)
    }
}

async function getCategories() {
    try {
        let response = await fetch(`${BASE_API}/products/categories`)
        let categories = await response.json()

        categories.forEach(category => {
            containerCategories.innerHTML += `
                <label>
                    <input name="category" oninput="filterPerCategory()" type="checkbox"  value="${category}" />
                    ${category}
                </label>
            ` 
        })
        //TO-DO montar os inputs de categoria

    } catch (error) {
        console.error(error)
    }
}

getCategories()
getProducts()