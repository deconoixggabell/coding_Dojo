console.log(document)
// option 1
// let number = document.getElementsByClassName("counting_num")[0]

// option 2
let number = document.querySelector(".counting_num")

function alartme(){
    alert("hello World")
}

function increasenum(num){
    console.log(num)
    console.log(num.innerText)
    // console.log(typeof(num.innerText))
    num.innerText = parseInt(num.innerText) + 1
}

console.log()
function increasenum2(){
    number.innerText = parseInt(number.innerText) + 1
}