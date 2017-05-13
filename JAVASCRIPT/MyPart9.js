var firstName;
var lastName;
var age;
var tall;
var petName;

alert("Hello, you are sfigato but maybe you can answer some question!")
firstName = prompt("What's is your firstname?");
lastName = prompt("What's is your lastName?");
age = prompt("How old are you?");
tall = prompt("How tall are you?");
petName = prompt("What is the name of your pet");

var nameCond = false;
var ageCond = false;
var tallCond = false;
var petNameCond = false;

if (firstName.charAt(0) == lastName.charAt(0) ) {
  nameCond = true;
  if (age > 20 && age < 30) {
    ageCond = true;
    if (tall >= 170) {
      tallCond = true;
      if (petName[petName.length -1] == "y") {
        petNameCond = true;
        console.log("Hello comrad, you are in!");
      }
    }
  }
}

alert("Ehmhm there are some problem!")

if (nameCond == false) {
  alert("Hai un nome del cavolo");
}
if (ageCond == false) {
  alert("sei un bimbominchia");
}
if (tallCond == false) {
  alert("sei troppo basso");
}
if (petNameCond == false) {
  alert("tuo pet è una merda");
}
