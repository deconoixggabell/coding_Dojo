let number = document.querySelector(".in-like")

function like(){
    number.innerText = parseInt(number.innerText) + 1 + ' Like(s)'
}