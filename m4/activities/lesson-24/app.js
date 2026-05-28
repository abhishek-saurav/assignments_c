function log(msg) {
  document.getElementById("out").innerHTML += msg + "<br>";
}

var userName = "Sam";
var userAge = 15;
var userCity = "Bangalore";

log("Name: " + userName);
log("Age: " + userAge);
log("City: " + userCity);
log("");
log("This code is in an external JS file!");
