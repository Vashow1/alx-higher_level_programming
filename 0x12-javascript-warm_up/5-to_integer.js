#!/usr/bin/node

const foo = parseInt(process.argv[2]);
if (isNaN(foo)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + foo);
}
