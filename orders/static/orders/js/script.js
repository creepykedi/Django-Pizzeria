/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}
let btn = document.getElementById("make-order");


$(document).ready(function() {
  $("#wow").click(function(){
    $("#wow").hide(1000);
  });
});


$(function() {
  rowscount = $('.order-row').length;
  console.log(rowscount);
  let x;
  for (x =0 ; x < rowscount; ) {
  item = $('.order-item')[x].textContent;
  toppings = $('.chosen-toppings')[x].textContent;
  item_num = item.replace(/[^0-9]/g, '');
  console.log(item_num);
  select_button = $(".choose-topping");
  selection_dropdown = $(".select-topping-field");
  console.log(item, toppings);
  x++;
  if (item_num == toppings.split(",").length) {
    if (toppings != '') {
          select_button.eq(x-1).hide();
          selection_dropdown.eq(x-1).hide();
    }
}}});

