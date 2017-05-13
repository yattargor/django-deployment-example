// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = [];

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array

function addNew(name){
  var name = prompt("What name do you want add in this roster?");
  roster.push(name);
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript

function remove(name){
  var name = prompt("What name do you want remove from this roster?");
  for(var i = roster.length - 1; i >= 0; i--) {
    if(roster[i] === name) {
       roster.splice(i, 1);
    }
  }
}



// DISPLAY ROSTER

// Create a function called display that prints out the roster to the console.

function display(){
  for (name of roster) {
    console.log(name);
  }
}

// Start by asking if they want to use the web app
alert("Welcome to my webapp");
var start = prompt("Hello do you want use this webapp? answer Y or N");

while (start == "Y" || start == "y") {
    var action = prompt("What action doy you want? Answer add,remove,display or quit");
    if (action == "add") {
      addNew();
      //console.log(addNew(nameIn));
    }else if (action == "remove") {
      remove();
      //console.log(remove(nameOut));
    }else if (action == "display") {
      display();
      //console.log(display());
    } else if (action == "quit") {
      alert("Now I quit this webapp");
      start = "R";
    }else {
      alert("I don't recognized your input");
      start = "Y";
    }
}
if(start == "N" || start == "n"){
  alert("Answer with correct letters! Refresh page to rebegin")
} else if (start == "R") {
  alert("Refresh page to rebegin");
}


// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
