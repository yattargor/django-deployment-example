//FOR LOOPS
var word = "Hello";
var x = 0;

for (var i = 0; i < 5; i++) {
  console.log(word);
}

while (x < 5) {
  console.log(word);
  x++;
}

var num = 0;
var numWhile = 0;

for (var i = 0; i <= 25; i++) {
  if (num%2 !== 0) {
    console.log(num);
  }
  num++;
}

while (numWhile <= 25) {
  if (numWhile%2 !== 0) {
    console.log(numWhile);
  }
  numWhile++;
}
