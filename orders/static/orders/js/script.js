/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

let btn = document.getElementById("make-order");

btn.addEventListener("click", function () {
  let ourRequest = new XMLHttpRequest();
  ourRequest.open('GET','https://learnwebcode.github.io/json-example/animals-1.json' );
  ourRequest.onload = function () {
    let ourData = JSON.parse(ourRequest.responseText);
  };
  ourRequest.send()
});
