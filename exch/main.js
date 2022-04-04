// create two boxes
//create drop down lists
// need currency info.
// whn currency input
let currencyRatio = {
    USD: {
        KRW: 1218,
        USD: 1,
        YEN: 122.51,
        Unit: "Dollar"
    },
    KRW: {
        KRW: 1,
        USD: 0.00082,
        YEN: 0.10,
        Unit: "Won"
    },
    YEN: {
        YEN: 1,
        USD: 0.0082,
        KRW: 9.96,
        Unit: "Yen"
    },
};
let fromCurrency = "USD";
let ToCurrency = "USD";
//console.log(currencyRati =.USD.Unit)
//currencyRatio.USD.Unit
document.querySelectorAll("#from-currency-list a").forEach((menu) =>
    menu.addEventListener("click", function () {
        //bring a button from the list and change a value for the button.
        //The getElementById() method returns an element with a specified value. 
        document.getElementById("from-button").textContent = this.textContent;
        //store value in the selected currency
        fromCurrency = this.textContent;
        convert()
    })
);
document.querySelectorAll("#to-currency-list a").forEach((menu) =>
    menu.addEventListener("click", function () {
        //bring a button from the list and change a value for the button.
        //The getElementById() method returns an element with a specified value. 
        document.getElementById("to-button").textContent = this.textContent;
        //store value in the selected currency
        ToCurrency = this.textContent;
        convert()
    })
);
//to do list
//

function convert() {
    //currency
    //how much? 
    // money*currency
    let amount = document.getElementById("from-input").value;
    let converted_amount = amount * currencyRatio[fromCurrency][ToCurrency];
    //console.log("the converted amount", converted_amount)
    document.getElementById("to-input").value = converted_amount;
}
function 