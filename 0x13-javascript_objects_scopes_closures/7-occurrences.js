#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  occurences = 0;
  for (let i = 0; list[i]; i++) {
    if (searchElement === list[i]) {
      occurences++;
    }
  }
  return (occurences);
};
