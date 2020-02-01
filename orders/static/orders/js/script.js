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
  let z; z=0; //z is adjuster
  for (x = 0 ; x < rowscount; ) {
     if(typeof($('.order-item')[x]) != 'undefined'||null) {
        if ($('.order-item')[x].textContent.replace(/[^0-9]/g, '').length) {
        item = $('.order-item')[x].textContent;
        item_num = item.replace(/[^0-9]/g, ''); //getting max number of toppings that is in chosen item
        toppings = $('.chosen-toppings')[x-z].textContent;}
     // if there are no toppings, increase loop iterator, increase adjuster Z and skip this iteration
        else {x++;z++;
         continue}
     }

    select_button = $(".choose-topping");
    selection_dropdown = $(".select-topping-field");
    orderBtn =  $("#make-order-link");
    clearBtn = $(".clear-topping")[x-z];
    x++;

    // if number of chosen toppings and maximum matches, hide selector
    if (item_num == toppings.split(",").length) {
      if (toppings != '') {
            select_button.eq(x-1-z).hide();
            selection_dropdown.eq(x-1-z).hide();
      }
} //if any selectors aren't hidden, mute order button
   if ($(select_button.eq(x-1-z)).is( ":visible")) {
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