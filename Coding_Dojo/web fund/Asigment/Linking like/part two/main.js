console.log("running JS")

let number = document.querySelector(".in-like")
let number1 = document.querySelector(".in-like-1")
let number2 = document.querySelector(".in-like-2")

// this controls the first button
function like(){
    number.innerText = parseInt(number.innerText) + 1 + ' Like(s)'
}

// this controls the second button
function like_1(){
    number1.innerText = parseInt(number1.innerText) + 1 + ' Like(s)'
}

// this controls the third button
function like_2(){
    number2.innerText = parseInt(number1.innerText) + 1 + ' Like(s)'
}