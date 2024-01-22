
// get the stars //

const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('rate-form')

// Listen for click event //

const handleStarSelect = (size) => {
    const children = form.children
    for(let i=0; i < children.length; i++) {
        if(i<= size) {
            children[i].classList.add('checked')   
        } else {
        children[i].classList.remove('checked')
    }
  } 
}

// how many stars should chnage colour.. example 5 star rating would be 5 stars. //

const handleSelect = (selection) =>{
    switch(selection){
        case 'first' : {
            handleStarSelect(1)
            return
        
        }

        case 'second' : {
            handleStarSelect(2)
            return
    }
        case 'third' : {
            handleStarSelect(3)
            return
        }

        case 'fourth' : {
            handleStarSelect(4)
            return
        }

        case 'fifth' : {
            handleStarSelect(5)
            return
        }
    }
}

