/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}
let btn = document.getElementById("make-order");


// function to hide topping selection if all are chosen
$(function() {
  rowscount = $('.order-row').length;
  console.log(rowscount);
  let x; // x is a row index

  for (x = 0 ; x < rowscount; ) {
      console.log('here');
 if(typeof($('.order-item')[x]) != 'undefined') {
    item = $('.order-item')[x].textContent;
    toppings = $('.chosen-toppings')[x].textContent;}
    item_num = item.replace(/[^0-9]/g, ''); //getting max number of toppings that is in chosen item
    select_button = $(".choose-topping");
    selection_dropdown = $(".select-topping-field");
    orderBtn =  $("#make-order-link");
    clearBtn = $(".clear-topping")[x];
    x++;

    console.log("iteration " + (x-1), select_button.eq(x-1),"x-n is " + (x-1) );
    console.log("toppings length " + toppings.split(",").length +" chosen length" + item_num + " " + item + " /" + toppings) ;

    // if number of chosen toppings and maximum matches, hide selector
    if (item_num == toppings.split(",").length) {
      if (toppings != '') {
            select_button.eq(x-1).hide();
            selection_dropdown.eq(x-1).hide();
      }
} //if any selectors aren't hidden, mute order button
   if ($(select_button.eq(x-1)).is( ":visible")) {
        orderBtn.addClass('disabled');
      }
  }
});

/* AJAX add to cart
$(".addToCart").click(function () {
    let buyer;
    buyer = $(this).attr("data-buyer");
    $.get('/item/add/(?P<item_id>[-\w]+)/',{})
}) */