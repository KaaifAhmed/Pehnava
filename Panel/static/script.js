// document.getElementById("Products").addEventListener("click", function(){
//     document.getElementById("Productsdesc").classList.toggle("none");
// })
// document.getElementById("Navbar").addEventListener("click", function(){
//     document.getElementById("Navbardesc").classList.toggle("none");
// })
//  document.getElementById("Categories").addEventListener("click", function(){
//      document.getElementById("Categoriesdesc").classList.toggle("none");
// })
// document.getElementById("Images").addEventListener("click", function(){
//     document.getElementById("Imagesdesc").classList.toggle("none");
// })
// document.getElementById("News").addEventListener("click", function(){
//     document.getElementById("Newsdesc").classList.toggle("none");
// })
// document.getElementById("Order").addEventListener("click", function(){
//     document.getElementById("Orderdesc").classList.toggle("none");
// })




// the above code was so errorneous




function expand(id) {
    document.getElementById(id).classList.toggle("none");
}

const pages_names = ["Order", "Categories", "UI Config", "Product-Vis-Section", "Analytics", "Models-integration"];
var non_none = "Product-Vis-Section"

function render (id) {
    
    document.getElementById(id).classList.toggle("none");
    document.getElementById(non_none).classList.toggle("none");
    non_none = id;
}
