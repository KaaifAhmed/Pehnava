var searchElement = document.getElementById('search');
document.getElementById('search-link').addEventListener('click', searchPop);

document.getElementById('search-cross').addEventListener('click', searchExit);

document.getElementById('search-btn').addEventListener('click', search);

function searchPop() {
    searchElement.style.transform = 'translateY(0)';    
    searchElement.style.opacity = '1';    
}

function searchExit() {
    searchElement.style.transform = 'translateY(-100%)';    
    searchElement.style.opacity = '0';    
}

function search() {
    document.location.href = "../search/"
}

function footerHandling() {
    
    let title = document.getElementsByClassName("results-head").item(0);
    let footer = document.getElementsByTagName('footer').item(0);
    console.log(footer);
    
    if (document.body.clientWidth > 458) {
        if (title.innerHTML.slice(0, 5) == "Oops!" || title.innerHTML.slice(0, 2) == 'No') {
            footer.style.position = 'fixed';
            footer.style.bottom = '0';
        } else {
            footer.style.position = 'relative';
            // footer.style.bottom = '0';
            
        }
    }
}

footerHandling();



