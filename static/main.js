'use strict';


function showform(dowhat) {
    /*
    * four DIVS: browse, insert, update, delete
    * this function sets one visible the others not
    */
    if(dowhat == 'insert') {
        document.getElementById('browse').style.display = 'block';
        document.getElementById('insert').style.display = 'block';
    }  else { //by default display browse
        document.getElementById('browse').style.display = 'block';
        document.getElementById('insert').style.display = 'none';
    }
}


function insert() {
    showform('insert');
}

function browse() {
    showform('browse');
}

// function today() {
//     document.getElementById('transactionDate').valueAsDate = new Date();
//     document.getElementById('transactionTime')
// }

// function addProduct(){
//     productPlaceholder = document.getElementById('productPlaceholder')

//     productPlaceholder.value += `
//     <p>Select another product.</p>
//     <select>
//         {% for item in data %}
//             <!-- Create a <option> element with the value of that key in it -->
//             <option value="{{item["productID"]}}">{{item["name"]}}</option>
        
//             <!-- End of this for loop -->
//         {% endfor %}
//     {% endwith %}
//     </select>`

// console.log("Adding Product")
// }


// LISTEN to the events
document.addEventListener('DOMContentLoaded', () => {
    showform('browse');


    const insertButton = document.getElementById('add_new');
    insertButton.addEventListener('click', insert);

    const cancelButton = document.getElementById('cancel');
    cancelButton.addEventListener('click', browse);

    // if (document.getElementById('addProduct')){
    //     const addProductButton = document.getElementById('addProduct');
    //     addProductButton.addEventListener('click', addProduct);
    // }

});