//Lembrete: se for uma classe usamos o '.' na frente e se for um id usamos '#'
//Por convenção, para indicar valores fixos, colocamos letra maiúscula

const shoppingCartQuantity = document.querySelector(".shoppingCartQuantity")
const containerCategories = document.querySelector(".categories")
const containerProducts = document.querySelector(".productsList")
const containerCart = document.querySelector(".cartItems")
const BASE_API = "https://fakestoreapi.com"

let storageCart = localStorage.getItem('shoppingCart')

let shoppingCart = storageCart ? JSON.parse(storageCart) : [] 
let products = []
shoppingCartQuantity.innerHTML = shoppingCart.length

function saveInStorage() {
    localStorage.setItem('shoppingCart', JSON.stringify(shoppingCart))

    containerCart.innerHTML = ''

    shoppingCart.forEach(item => {
        containerCart.innerHTML += `
             <div class="cartProduct">
                <img src="${item.image}" />

                <div class="quantity">
                    <button onclick="decreaseQuantity(${item.id})">-</button>
                    <input type="text" readonly value="${item.quantity}"/>
                    <button onclick="increaseQuantity(${item.id})">+</button>
                </div>

                <p>R$ ${item.price.toFixed(2)}</p>
            </div>
        `
    })
}

function decreaseQuantity(itemId) {
    // Procurar o item no carrinho para verificar a quantidade 
    // se por um acaso a quantidade do item for 1, eu vou retirar ele do array carrinho
    //filter

    // Se a quantidade ainda for maior que 1, eu diminuo a quantidade normalmente
    //Atualizo a tela para o usuario ver e salvo no armazenamento local
}

function increaseQuantity(itemId) {
    shoppingCart = shoppingCart.map(item => {
        if (item.id === itemId) {
            item.quantity += 1
        }
        return item;
    })

    saveInStorage()
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
    containerProducts.innerHTML = ''

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

    saveInStorage()

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
    const checkedInputs = document.querySelectorAll("input[name=category]:checked")
    const filters = [...checkedInputs].map(input => input.value)

    const filteredProducts = products.filter(product => filters.includes(product.category))

    showProducts(filters.length > 0 ? filteredProducts : products)
}

getCategories()
getProducts()
saveInStorage()