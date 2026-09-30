function addToCart(productName, price) {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    cart.push({
        name: productName,
        price: price
    });

    localStorage.setItem("cart", JSON.stringify(cart));

    alert(productName + " added to cart!");
}
function loadCart() {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    let cartItems = document.getElementById("cart-items");
    let cartTotal = document.getElementById("cart-total");

    let total = 0;

    cartItems.innerHTML = "";

    cart.forEach(function(product) {
        let item = document.createElement("p");

        item.textContent = product.name + " - $" + product.price;

        cartItems.appendChild(item);

        total += product.price;
    });

    cartTotal.textContent = "Total: $" + total;
}
function setupCheckout() {
    let form = document.getElementById("checkout-form");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        window.location.href = "confirmation.html";
    });
}