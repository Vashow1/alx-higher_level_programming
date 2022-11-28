#!/usr/bin/node

const foo = parseInt(process.argv[2]);

if (isNaN(foo)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < foo; i++) {
    for (let j = 0; j < foo; j++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
