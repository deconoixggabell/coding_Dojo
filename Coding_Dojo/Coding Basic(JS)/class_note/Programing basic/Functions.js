// Functions

// function helloworld(){
//     console.log("hello world")
// }

// // call function
// helloworld()


// function helloworld(name,age){
    // console.log("hello world")
//     console.log(name, age)
// }

// helloworld("gloire", 5)

// function helloworld(name="deconoix",age=5){
//     console.log("hello world")
//     console.log(name, age)
// }

// helloworld()


// function birthday(age=5){
//     console.log("Happy Birthday!")
//     return age + 1
// }

// let newage = birthday(30)
// console.log(newage)


function birthday(age=5){
    if(age < 30){
        return "happy Birthday live it up"
    }
    else {
        return "return to bed"
    }
}

let newage = birthday(30)
console.log(newage)