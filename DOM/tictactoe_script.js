var td11 = document.getElementById("1-1");
var td12 = document.getElementById("1-2")
var td13 = document.getElementById("1-3")

var td21 = document.getElementById("2-1")
var td22 = document.getElementById("2-2")
var td23 = document.getElementById("2-3")

var td31 = document.getElementById("3-1")
var td32 = document.getElementById("3-2")
var td33 = document.getElementById("3-3")

//Restart Game button
var restart = document.querySelector("#Refresh");
var squares = document.querySelectorAll(".slotsize");

function clearBoard(){
    //Loop inside every elements in array "squares"
    for (var i = 0; i < squares.length; i++) {
      squares[i].textContent = " ";
    }
}

restart.addEventListener("click", clearBoard);

//Second solution to fill square with for loop
for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener("click", changeMarker);
}

function changeMarker(){
        if (this.textContent == " ") {
          this.textContent = "O";
        }else if (this.textContent == "O") {
          this.textContent = "X";
        }else {
          this.textContent = " ";
        }
}



// td11.addEventListener("click", function(){
//   if (this.textContent == " ") {
//     this.textContent = "O";
//   }else if (this.textContent == "O") {
//     this.textContent = "X";
//   }else {
//     this.textContent = " ";
//   }
// })
//
// td12.addEventListener("click", function(){
//   if (this.textContent == " ") {
//     this.textContent = "O";
//   }else if (this.textContent == "O") {
//     this.textContent = "X";
//   }else {
//     this.textContent = " ";
//   }
// })
//
// td13.addEventListener("click", function(){
//   if (this.textContent == " ") {
//     this.textContent = "O";
//   }else if (this.textContent == "O") {
//     this.textContent = "X";
//   }else {
//     this.textContent = " ";
//   }
// })
//
// td21.addEventListener("click", function(){
//   if (this.textContent == " ") {
//     this.textContent = "O";
//   }else if (this.textContent == "O") {
//     this.textContent = "X";
//   }else {
//     this.textContent = " ";
//   }
// })
//
// td22.addEventListener("click", function(){
//   if (this.textContent == " ") {
//     this.textContent = "O";
//   }else if (this.textContent == "O") {
//     this.textContent = "X";
//   }else {
//     this.textContent = " ";
//   }
// })
//
// td23.addEventListener("click", function(){
//   if (this.textContent == " ") {
//     this.textContent = "O";
//   }else if (this.textContent == "O") {
//     this.textContent = "X";
//   }else {
//     this.textContent = " ";
//   }
// })
//
// td31.addEventListener("click", function(){
//   if (this.textContent == " ") {
//     this.textContent = "O";
//   }else if (this.textContent == "O") {
//     this.textContent = "X";
//   }else {
//     this.textContent = " ";
//   }
// })
//
// td32.addEventListener("click", function(){
//   if (this.textContent == " ") {
//     this.textContent = "O";
//   }else if (this.textContent == "O") {
//     this.textContent = "X";
//   }else {
//     this.textContent = " ";
//   }
// })
//
// td33.addEventListener("click", function(){
//   if (this.textContent == " ") {
//     this.textContent = "O";
//   }else if (this.textContent == "O") {
//     this.textContent = "X";
//   }else {
//     this.textContent = " ";
//   }
// })
