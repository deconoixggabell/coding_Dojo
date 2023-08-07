// Function Declaration
function add2(num) {
    return  num + 2;
}

console.log(add2(5))

// Functions "are first class citizen in JS = "

//Function express
const add2expression = function(num){
    return num + 2
};
const result = add2expression(10)
console.log(result)


// arrow function
const add2arrow = (num) => num + 2;
const result2 = add2arrow(2)
console.log(result2)

// option 2
const add2Nums = (num1, num2) =>{
    const sum = num1 + num2
    return sum
}
const result3 = add2Nums(2, 2)
console.log(result3)

//higher order function and callback function
function filter(arr, cb){
    const newArr= [];;
    for (const item of arr){
        if(cb(item)){
            newArr.push(item);
        }
    }
    return newArr;
}

//callback function
const isEven = (num) => num % 2 == 0;
const isOdd = (num) => num % 2 !== 0;

const oneToTen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

const evens = filter(oneToTen, isEven);
console.log(evens);

const odds = filter(oneToTen, isOdd);
console.log(evens);


// forEach, map. filter
// .forEach
oneToTen.forEach((item) => {
    console.log(item)
});

//map
// oneToTen.map( (item) => {
//     const listItems = oneToTen.map
//     return `<li>Item # ${item}</li>`
// })

// // fillter
// const muppets = [
//     {
//         id: 1,
//         name: 'kermit',
//     };
//     {
//         id: 2,
//         name: 'gonzo',
//     };
//     {
//         id: 3,
//         name: 'rowlf',
//     };
// ];

// const piggy = muppets.filter((muppets) => muppets.id === 3)
// console.log(piggy)

// asynchonous functions



// setTimeout
let greeting;

setTimeout(() => {
    greeding = 'hello';
}, 2000);

console.log(greeting);
// fetch