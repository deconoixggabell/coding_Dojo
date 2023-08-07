// the four pillars of OOP

//Encapsulation
// - Gronp related variables and functions together

//abstraction
// - hide the details and complesity and show only the essentials

// inheritance
// - Eliminate reuntant code

//Polymorohyism
// - refactor ugly switch/case statements
// - allows me to change behavior or implement methods in child classas


// // create a car object
// let car1 = {
//     make; "BMW"
//     model: "75li"
//     year: 2023
// }
// let car1 = {
//     make; "BMW"
//     model: "75li"
//     year: 2023
// }
// let car1 = {
//     make: "BMW"
//     model: "75li"
//     year: 2023
// }





// class car {
//     constructor(make, model, year){
//     this.make = make;
//     this.model = model;
//     this.year = year;
// }
//     Print(){
//     console.log(`${this.make} ${this.model} ${this.year}`)
// }
// }

// // create car one
// let myCar1 = new car("BMW", "35353h", "2023")
// let myCar2 = new car("toyota", "5553h", "2016")

// // Print the car object
// myCar1.Print()
// myCar2.Print()

//create bank account

class BankAccount{
    constructor(accountNumber, AccountHolder, AccoutBalance){
        this.AccountHolder = AccountHolder;
        this.AccoutBalance = AccoutBalance;
        this.accountNumber = accountNumber;
    }
    deposit(amount){
        this.AccoutBalance += amount;
    }
    withdraw (amount){
        this.AccoutBalance -= amount;
    }
    // gainInterst(){
    //     this.AccoutBalance *= 1.05;
    // }
    // transfer(amount, account){
    //     this.AccoutBalance -= ;
    //     this.AccoutBalance 
    // }
}


let bank1 = new BankAccount(4422446, "Jon jo", 1000)
console.log(bank1.AccoutBalance);
bank1.deposite(500);
console.log(bank1.AccoutBalances);
bank1.withdraw(100)
console.log(bank1.AccoutBalance)

