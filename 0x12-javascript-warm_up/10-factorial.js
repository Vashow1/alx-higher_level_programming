#!/usr/bin/node

let foo = parseInt(process.argv[2]);

if (isNaN(foo)) {
  foo = 1;
}
function factorial (foo) {
  if (foo === 0) {
    return (1);
  }
  return (foo * factorial(foo - 1));
}
console.log(factorial(foo));
