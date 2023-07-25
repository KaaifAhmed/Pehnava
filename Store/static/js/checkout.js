var item = JSON.parse((localStorage.getItem(localStorage.key(0))))


document.getElementById('cartSection').innerHTML = `<div class="items"><div class="item"><img src="${item.img}" alt=""><p class="item-badge" id="cart-qty">${item.qty}</p><span class="item-detail"><h6 class="item-name" id="cart-product-name" > ${item.name}</h6><p class="item-price" id="cart-price-ind">PKR. ${item.ind_price}</p></span></div><div class="pricing"><span class="subtotal"><p>Subtotal</p><h6 id="cart-price-net">PKR. ${item.net_price}</h6></span><span class="delivery"><p>Delivery</p><h6 id='delievery-price'>PKR. ${item.delievery}</h6></span><span class="total"><p>Total</p><h6 >PKR.  ${item.net_price+item.delievery}</h6></span></div></div>`;
console.log(item);


document.addEventListener('DOMContentLoaded', function() {
  
    document.getElementById("acutal_cart").setAttribute('value', localStorage.getItem(localStorage.key(0)))

});

