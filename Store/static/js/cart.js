const cart = {};
var cartitem;
var delievery_price = 50
class Desc {
    constructor(itemname, qty, individual_price, net_price, color, size, img, dp) {
    this.name = itemname
    this.qty = qty;
    this.ind_price = individual_price;
    this.net_price = net_price;
    this.img = img
    this.color = color;
    this.size = size;
    this.delievery = dp
    }
}

function addToCart (itemname,...kwargs) {
    const item = new Desc(itemname, ...kwargs)
    cartitem = null;
    localStorage.clear()
    // location.reload()
    localStorage.setItem(itemname, JSON.stringify(item));
    cartitem = item;
}




// Rites function starting -----------------------------


function proceed () {


    itemname = document.getElementById('pr-name').innerText;
    qty = document.getElementById('prod-qty').innerText;
    ind_price = document.getElementById('pr-price').innerText;
    net_price = parseInt(qty)*parseInt(ind_price)
    color = null;
    size = $('#product-sizes .selected-size');
    

   
    img = document.getElementById('main-img').src;


    addToCart(itemname, qty, ind_price, net_price, color,size.text() ,img, delievery_price);
    
    document.location.href = '../checkout'
}
