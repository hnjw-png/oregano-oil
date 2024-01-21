
// get the stars //

const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('rate-form')
const confirmbox = document.getElementById('confirm-box')

const csrf = document.getElementById('csrfmiddlewaretoken')

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

const getNumberValue = (stringValue) =>{
    let NumberValue;
    if (stringValue === 'first') {
        NumberValue = 1
    }
    else if (stringValue == 'second') {
        NumberValue = 2
    }
    else if (stringValue == 'third') {
        NumberValue = 3
    }
    else if (stringValue == 'fourth') {
        NumberValue = 4
    }
    else if (stringValue == 'fifth') {
        NumberValue = 5 
    }
    else {
        NumberValue = 0
    }
}
if(one) {
const arr = [one, two, three, four, five]

arr.forEach(item> item.addEventListener('mouseover', (event)=>{
    handleSelect(event.target.id)
}))

arr.forEach(item> item.addEventListener('click', (event)=>{
    const val = event.target.id

    form.addEventListener('submit', e=>{
        e.preventDefault()
        const id = e.target.id
        const_val_num = getNumberValue(val)


    })
}))

}
