// //1
// for (let x=3; x < 8; x+2){
//     console.log(x)
// }

// //8
// function sum_odd(start, end){
//     let oddnumber = []
//     for (let i = start; i <= end; i++){
//         if(i%2 == 1){
//             oddnumber.push(i)
//         }
//     }
//     return oddnumber
// }

// console.log(sum_odd(12,30))

// 8 ***
// function sum_odd(){
//     let sum =0
//     for (i = 12; i <=30; i++){
//         if (i%2 ==1){
//             sum = sum +i
//         }
//     }


//     return sum
// }

// console.log(sum_odd())

// // 9
// function rangeeofarray(){
//     var array = [-13,-15,-8,-29,-3,4,9,-3,7]
//     var smallest =[0]
//     var largest = [0]

//     for (let i = 1; i < array.length; i++){
//         if(array[i] < smallest){
//             smallest = array[i]
//         }
//         else if(array[i]  > largest){
//             largest = array[i]
//         }
//     }

//     return larest - smallest;
// // }
// var msg = 'hello'

// for(var x = 15; x > msg.length + 4; x -= 3){
//     console.log(x)
// }

var array = [5,3,4,1];

for(var x = 0; x < array.length; x++){
    for( var y = array.length - 1; y >= x; y--){
        if (array[x] > array[y]){
            var temp = array[y];
            array[y] = array[x];
            array[x] = temp;
        }
    }
}

console.log(array)