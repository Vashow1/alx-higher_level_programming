#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const sortedAr = process.argv.slice(2).map(function (x) {
    return parseInt(x);
  });
  console.log(sortedAr.sort(function (a, b) { return b - a; })[1]);
}
