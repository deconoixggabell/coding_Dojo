let wave1 = document.querySelector('.itme_1')
let wave2 = document.querySelector('.itme_2')
let wave3 = document.querySelector('.itme_3')


function increasewave(element){
    if ( element == 'item_1'){
    wave2.innerText = parseInt(wave1.innerText) + 1
    }
    else if(element == 'item_1'){
        wave2.innerText = parseInt(wave2.innerText) + 1
    }
    else{
        wave3.innerText = parseInt(wave3.innerText) + 1
    }
}