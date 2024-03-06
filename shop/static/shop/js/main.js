if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
}

// ------------------  Adding to cart functionality  ----------------//

$(document).on('click', '.atc', function () {
    var item_id = this.id.toString();
    console.log(item_id);

    if (cart[item_id] != undefined) {
        // if the item already exists
        quantity = cart[item_id][0] + 1;
        cart[item_id][0] = quantity;
        cart[item_id][2] = cart[item_id][2] + parseFloat(document.getElementById('price' + item_id).innerHTML);
    } else {
        // adding the item for the first time
        quantity = 1;
        price = parseFloat(document.getElementById('price' + item_id).innerHTML);
        names = document.getElementById('nm' + item_id).innerHTML;
        cart[item_id] = [quantity, names, price];
    }
    console.log(cart);
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = '<i class="bi bi-cart3"></i>(' + Object.keys(cart).length + ')';

})

let total = 0
for (item in cart) {
    let title = cart[item][1];
    let quantity = cart[item][0];
    let price = cart[item][2];
    total += cart[item][2];

    itemString = `<li class="list-group-item d-flex justify-content-between align-items-start">
                    <div class="ms-2 me-auto">
                        <div class="">${title} (${quantity})</div>
                    </div>
                    <span class="badge ba text-dark">$ ${price}</span>
                </li>`
    $('#item_list').append(itemString);
}

totalPrice = `<li class="list-group-item d-flex justify-content-between align-items-start">
                    <div class="ms-2 me-auto">
                        <div class="fw-bold">Total</div>
                    </div>
                    <span class="badge ba text-dark">$ ${total}</span>
                </li>`
$('#item_total').append(totalPrice);
$('#items').val(JSON.stringify(cart));
$('#total').val(total)