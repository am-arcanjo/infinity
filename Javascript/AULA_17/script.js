//Lembrete: se for uma classe usamos o '.' na frente e se for um id usamos '#'
//Por convenção, para indicar valores fixos, colocamos letra maiúscula

const shoppingCartQuantity = document.querySelector(".shoppingCartQuantity")
const containerCategories = document.querySelector(".categories")
const containerProducts = document.querySelector(".productsList")
const BASE_API = "https://fakestoreapi.com"

let storageCart = localStorage.getItem('product')

let shoppingCart = storageCart ? JSON.parse(storageCart) : [] 
let products = []

function saveInStorage() {
    localStorage.setItem('product', JSON.stringify(shoppingCart))
}

async function getProducts() {
    try {
        let response = await fetch(`${BASE_API}/products`)
        let data = await response.json()

        products = data

        showProducts()
    } catch (error) {
        console.error(error)
    }
}

function showProducts(productsArray = products) {
    containerProducts.innerHTML = '-'

    productsArray.forEach(product => {
        containerProducts.innerHTML += `
        <div class="product">
            <img src="${product.image}" />
            <h4>${product.title}</h4>
            <div>
                <p>R$ ${product.price}</p>

                <button onclick="addInShoppingCart(${product.id})">
                    <img class="shoppingCartForProduct" width="25" height="25" src="./shoppingCart.svg" alt="shopping-cart-loaded--v1"/>
                </button>
            </div>
        </div>
        `
    })
}

function addInShoppingCart(idProduct) {
    const productInCart = shoppingCart.find(item => item.id === idProduct)

    if (productInCart) {
        shoppingCart = shoppingCart.map(item => {
            if (item.id === idProduct) {
                item.quantity += 1
            }

            return item
        })

    } else {
        const product = products.find(item => item.id === idProduct)
        product.quantity = 1
    
        shoppingCart.push(product)
    }

    shoppingCartQuantity.innerHTML = shoppingCart.length

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
    } catch (error) {
        console.error(error)
    }
}

function filterPerCategory() {
    let checkedInputs = document.querySelectorAll("input[name=category]:checked")
    checkedInputs = [...checkedInputs].map(input => input.value)

    const filteredProducts = products.filter(products => checkedInputs.includes(products.categories))

    showProducts(checkedInputs.length > 0 ? filteredProducts : products);
}

getCategories()
getProducts()