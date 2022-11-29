#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('C');
        }
        process.stdout.write('\n');
      }
    }
  }
};
