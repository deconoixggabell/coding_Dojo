/*
I eanted to create a senario where we at a theme park.
There is a ride that has its parimenter in order to be able to ride the ride.
You must be at least 10 years of age to be able to ride it.
You must be at least 5ft in order to be able to ride it.
You must be 150 or below in order to ride the ride.
*/

/*
the next block of code is used to define variable
'age' 'height' 'weight'
for all the perimiter we are using numerical variable
*/
let age = 10;
let height = 2;
let weight = 150;

/* 
here we are setting up the requerment.
the rider must be at least 10 years old & 5 feet & 150 ib
*/
if(age >= 10 && height >= 5 && weight <= 150){
    console.log("Enjoy the ride")
}
    //this checked if the rider is old enougth
    else if(age < 10){
        console.log("You do not meet the age requerment: ")
    }
        //this checks if the rider is tall enougth
        else if(height < 5){
            console.log("you do not meet the height requerment: ")
        }
            //this checks if the ride meets the weight rewuerment
            else if(weight > 151){
                console.log("you do not meet the weight requerment: ")
            }
                //if the rider doest meet any of the requerment than this line will print.
                else{
                    console.log("sorry you do noe meet any of the requerment: ")
                }


