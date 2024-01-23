
console.log('test')
// get the stars //

const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('.rate-form');
const confirmBox = document.getElementById('confirm-box');
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0];

// functions for event
const handleStarSelect = (size) => {
    const children = form.children
    for (let i = 0; i < children.length; i++) {
        if (i < size) {
            children[i].classList.add('checked');
        } else {
            children[i].classList.remove('checked');
        }
    }
};

// Event listeners for stars
const stars = [one, two, three, four, five];

stars.forEach(item => item.addEventListener('click', (event) => {
    handleSelect(event.target.id);
}));

// Submit form
form.addEventListener('submit', e => {
    e.preventDefault();
    const id = e.target.id;
    const value_number = getNumericValue;


});


// how many stars should change colour.. example 5 star rating would be 5 stars. //

const handleSelect = (selection) =>{
    switch(selection){
        case 'first' : {
            handleStarSelect(2)
            return
        }

        case 'second' : {
            handleStarSelect(3)
            return
    }
        case 'third' : {
            handleStarSelect(4)
            return
        }

        case 'fourth' : {
            handleStarSelect(5)
            return
        }

        case 'fifth' : {
            handleStarSelect(6)
            return
        }
    }
}

// get number of the star //

const getNumericValue = (stringValue) =>{
    let number;
    if (stringValue === 'first') {
        number = 1 
    }
    else if(stringValue === 'second')  {
        number = 2;
    }
    else if(stringValue === 'third')  {
        number = 3;
    }
    
    else if(stringValue === 'fourth')  {
        number = 4;
    }
    else if(stringValue === 'fifth')  {
        number = 5;
    }
    return number

}