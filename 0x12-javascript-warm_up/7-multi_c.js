#!/usr/bin/node

foo = parseInt(process.argv[2]);

if (isNaN(foo)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < foo; i++) {
    console.log('C is fun');
  }
}
